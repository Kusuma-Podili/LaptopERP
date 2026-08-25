from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import LaptopModel, LaptopUnit, Brand, ComponentItem, SerialLifecycleHistory
from .services.stock import StockService
from .services.serial import SerialLifecycleService


class LaptopModelListView(LoginRequiredMixin, ListView):
    model = LaptopModel
    template_name = 'inventory/model_list.html'
    context_object_name = 'laptop_models'
    paginate_by = 20

    def get_queryset(self):
        qs = LaptopModel.objects.select_related('brand', 'category', 'processor', 'ram', 'storage', 'display', 'gpu').all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(model_name__icontains=q)
        return qs


class LaptopModelDetailView(LoginRequiredMixin, DetailView):
    model = LaptopModel
    template_name = 'inventory/model_detail.html'
    context_object_name = 'model'


class LaptopUnitListView(LoginRequiredMixin, ListView):
    model = LaptopUnit
    template_name = 'inventory/unit_list.html'
    context_object_name = 'units'
    paginate_by = 25

    def get_queryset(self):
        qs = LaptopUnit.objects.select_related('laptop_model', 'laptop_model__brand').all()
        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)
        return qs


class SerialLookupView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/serial_lookup.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        query = self.request.GET.get('serial', '').strip()
        if query:
            unit = LaptopUnit.objects.filter(serial_number__iexact=query).select_related('laptop_model').first()
            ctx['unit'] = unit
            if unit:
                ctx['history'] = unit.history_logs.select_related('action_by').all()
            else:
                ctx['not_found'] = True
        return ctx


class StockValuationView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/stock_valuation.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['summary'] = StockService.get_inventory_summary()
        ctx['low_stock'] = StockService.get_low_stock_alerts()
        return ctx
