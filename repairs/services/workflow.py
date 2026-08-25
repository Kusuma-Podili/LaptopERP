from django.db import transaction
from decimal import Decimal
from ..models import WorkshopJobCard
from inventory.services.serial import SerialLifecycleService


class JobCardWorkflowService:
    @staticmethod
    @transaction.atomic
    def recalculate_costs(job_card):
        parts_total = sum(p.quantity * p.unit_cost_at_repair for p in job_card.parts_used.all())
        labor_hours = sum(log.hours_spent for log in job_card.labor_logs.all())
        hourly_rate = job_card.assigned_technician.hourly_rate if job_card.assigned_technician else Decimal('35.00')
        labor_total = labor_hours * hourly_rate

        job_card.total_parts_cost = parts_total
        job_card.actual_labor_hours = labor_hours
        job_card.total_labor_cost = labor_total
        job_card.total_repair_cost = parts_total + labor_total
        job_card.save(update_fields=['total_parts_cost', 'actual_labor_hours', 'total_labor_cost', 'total_repair_cost'])
        return job_card.total_repair_cost

    @staticmethod
    @transaction.atomic
    def complete_job_card(job_card, user):
        job_card.status = 'COMPLETED'
        job_card.save(update_fields=['status'])
        SerialLifecycleService.transition_status(
            job_card.unit,
            'IN_STOCK',
            user=user,
            location='Workshop Ready Bay',
            ref_doc=job_card.job_number,
            notes='Completed workshop diagnostic and repair'
        )
