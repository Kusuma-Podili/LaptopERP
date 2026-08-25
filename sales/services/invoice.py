from django.db import transaction
from django.utils import timezone
from decimal import Decimal
from ..models import Invoice, PaymentRecord


class InvoicingService:
    @staticmethod
    @transaction.atomic
    def record_payment(invoice, amount, payment_method, ref_no, user=None):
        receipt_no = f"RCT-{invoice.invoice_number}-{invoice.payments.count() + 1}"
        payment = PaymentRecord.objects.create(
            receipt_number=receipt_no,
            invoice=invoice,
            payment_method=payment_method,
            amount=amount,
            payment_date=timezone.now().date(),
            transaction_reference=ref_no
        )
        invoice.amount_paid = Decimal(str(invoice.amount_paid)) + Decimal(str(amount))
        if invoice.amount_paid >= invoice.total_amount:
            invoice.payment_status = 'PAID'
        elif invoice.amount_paid > 0:
            invoice.payment_status = 'PARTIAL'
        invoice.save(update_fields=['amount_paid', 'payment_status'])
        return payment
