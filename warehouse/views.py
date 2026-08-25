from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Warehouse, Zone, Bin, StockTransferOrder, CycleCount


class WarehouseListView(LoginRequiredMixin, ListView):
    model = Warehouse
    template_name = 'warehouse/warehouse_list.html'
    context_object_name = 'warehouses'


class BinMapView(LoginRequiredMixin, DetailView):
    model = Warehouse
    template_name = 'warehouse/bin_map.html'
    context_object_name = 'warehouse'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['zones'] = self.object.zones.prefetch_related('bins').all()
        return ctx


class TransferOrderListView(LoginRequiredMixin, ListView):
    model = StockTransferOrder
    template_name = 'warehouse/transfer_orders.html'
    context_object_name = 'transfers'
    paginate_by = 20


class CycleCountListView(LoginRequiredMixin, ListView):
    model = CycleCount
    template_name = 'warehouse/cycle_count.html'
    context_object_name = 'cycle_counts'
