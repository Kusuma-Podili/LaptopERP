from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Supplier, PurchaseOrder, GoodsReceiptNote, InwardQualityCheck


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'procurement/supplier_list.html'
    context_object_name = 'suppliers'


class PurchaseOrderListView(LoginRequiredMixin, ListView):
    model = PurchaseOrder
    template_name = 'procurement/po_list.html'
    context_object_name = 'orders'
    paginate_by = 20


class PurchaseOrderDetailView(LoginRequiredMixin, DetailView):
    model = PurchaseOrder
    template_name = 'procurement/po_detail.html'
    context_object_name = 'po'
