"""
Workshop SLA Tracking and Priority Escalation Engine.
Monitors job card turnaround times and escalates urgent repair orders.
"""

from django.utils import timezone
from datetime import timedelta
from repairs.models import WorkshopJobCard
from core.models import Notification, User


class RepairSLAEngine:
    SLA_HOURS_MAP = {
        'URGENT': 12,
        'HIGH': 24,
        'NORMAL': 48,
        'LOW': 72,
    }

    @classmethod
    def audit_sla_breaches(cls):
        now = timezone.now()
        escalated_jobs = []
        
        pending_jobs = WorkshopJobCard.objects.filter(
            status__in=['QUEUED', 'IN_DIAGNOSTICS', 'REPAIR_IN_PROGRESS']
        ).select_related('unit', 'assigned_technician')

        for job in pending_jobs:
            allowed_hours = cls.SLA_HOURS_MAP.get(job.priority, 48)
            sla_deadline = job.created_at + timedelta(hours=allowed_hours)
            
            if now > sla_deadline:
                if job.priority != 'URGENT':
                    job.priority = 'URGENT'
                    job.save(update_fields=['priority'])
                    escalated_jobs.append(job)
                    
                    if job.assigned_technician:
                        Notification.objects.create(
                            recipient=job.assigned_technician,
                            title=f"SLA Breach Escalation: Job #{job.job_number}",
                            message=f"Unit {job.unit.serial_number} exceeded {allowed_hours}h SLA limit. Priority escalated to URGENT.",
                            severity='DANGER'
                        )
        return escalated_jobs
