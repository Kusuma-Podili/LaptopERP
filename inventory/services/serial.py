"""
Serial Lifecycle State Machine and Verification Service.
"""

from django.db import transaction
from ..models import LaptopUnit, SerialLifecycleHistory


class SerialLifecycleService:
    @staticmethod
    @transaction.atomic
    def transition_status(unit, new_status, user=None, location=None, ref_doc='', notes=''):
        prev_status = unit.status
        unit.status = new_status
        if location:
            unit.current_location = location
        unit.save()

        SerialLifecycleHistory.objects.create(
            unit=unit,
            previous_status=prev_status,
            new_status=new_status,
            location=location or unit.current_location,
            action_by=user,
            reference_document=ref_doc,
            notes=notes
        )
        return unit
