from django.contrib import admin
from .models import WarrantyPolicy, ProductWarrantyRegistration, RMATicket

admin.site.register(WarrantyPolicy)
admin.site.register(ProductWarrantyRegistration)
admin.site.register(RMATicket)
