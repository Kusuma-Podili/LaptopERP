from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ProductWarrantyRegistration, RMATicket
from .services.rma import WarrantyValidationService
from inventory.models import LaptopUnit


class WarrantyLookupView(LoginRequiredMixin, TemplateView):
    template_name = 'warranty/warranty_lookup.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        serial = self.request.GET.get('serial', '').strip()
        if serial:
            unit = LaptopUnit.objects.filter(serial_number__iexact=serial).first()
            ctx['unit'] = unit
            if unit:
                ctx['is_valid'] = WarrantyValidationService.is_unit_under_warranty(unit)
                ctx['warranty'] = getattr(unit, 'warranty_record', None)
        return ctx


class RMATicketListView(LoginRequiredMixin, ListView):
    model = RMATicket
    template_name = 'warranty/rma_list.html'
    context_object_name = 'rma_tickets'
    paginate_by = 25
