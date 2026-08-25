from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer, SalesOrder, Invoice, PaymentRecord


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'sales/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 25


class SalesOrderListView(LoginRequiredMixin, ListView):
    model = SalesOrder
    template_name = 'sales/sales_orders.html'
    context_object_name = 'orders'
    paginate_by = 25


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = 'sales/invoice_detail.html'
    context_object_name = 'invoice'
