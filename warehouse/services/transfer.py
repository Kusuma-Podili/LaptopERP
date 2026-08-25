from django.db import transaction
from ..models import StockTransferOrder, StockTransferItem
from inventory.services.serial import SerialLifecycleService


class StockTransferService:
    @staticmethod
    @transaction.atomic
    def dispatch_transfer(transfer_order, user):
        transfer_order.status = 'IN_TRANSIT'
        transfer_order.save(update_fields=['status'])
        for item in transfer_order.items.select_related('unit').all():
            SerialLifecycleService.transition_status(
                item.unit,
                'IN_STOCK',
                user=user,
                location=f"In Transit to {transfer_order.destination_warehouse.name}",
                ref_doc=transfer_order.transfer_number,
                notes="In transit"
            )

    @staticmethod
    @transaction.atomic
    def receive_transfer(transfer_order, user):
        transfer_order.status = 'RECEIVED'
        transfer_order.received_by = user
        transfer_order.save(update_fields=['status', 'received_by'])
        for item in transfer_order.items.select_related('unit').all():
            item.is_received = True
            item.save(update_fields=['is_received'])
            SerialLifecycleService.transition_status(
                item.unit,
                'IN_STOCK',
                user=user,
                location=f"{transfer_order.destination_warehouse.name} Receiving",
                ref_doc=transfer_order.transfer_number,
                notes="Received at destination warehouse"
            )
