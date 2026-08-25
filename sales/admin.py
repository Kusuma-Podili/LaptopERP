from django.contrib import admin
from .models import Customer, TaxRule, SalesOrder, SalesOrderItem, Invoice, PaymentRecord

admin.site.register(Customer)
admin.site.register(TaxRule)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
admin.site.register(Invoice)
admin.site.register(PaymentRecord)
