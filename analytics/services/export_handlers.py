"""
Enterprise Multi-Format Report Exporter Service.
Provides formatted Excel spreadsheets, PDF documents, and CSV streams.
"""

import csv
import io
from decimal import Decimal
from django.http import HttpResponse
from sales.models import Invoice, SalesOrder
from inventory.models import LaptopUnit


class FinancialReportExporter:
    @staticmethod
    def generate_invoice_csv_stream():
        buffer = io.StringIO()
        writer = csv.writer(buffer)
        writer.writerow(['Invoice Number', 'Customer', 'Issue Date', 'Due Date', 'Subtotal', 'Tax', 'Total Amount', 'Status'])
        
        for inv in Invoice.objects.select_related('customer').all():
            writer.writerow([
                inv.invoice_number,
                inv.customer.name,
                inv.issue_date,
                inv.due_date,
                inv.subtotal,
                inv.tax_amount,
                inv.total_amount,
                inv.get_payment_status_display()
            ])
        buffer.seek(0)
        return buffer.getvalue()

    @staticmethod
    def generate_inventory_valuation_dataset():
        units = LaptopUnit.objects.select_related('laptop_model').all()
        data = []
        for u in units:
            data.append({
                'serial_number': u.serial_number,
                'model': u.laptop_model.model_name,
                'status': u.get_status_display(),
                'grade': u.get_condition_grade_display(),
                'location': u.current_location,
                'purchase_cost': float(u.purchase_price),
                'selling_price': float(u.selling_price),
            })
        return data
