from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from proveedores.views import InternalUserMixin
from .models import ProductReception

class InventoryEntryListView(LoginRequiredMixin, InternalUserMixin, ListView):
    model = ProductReception
    template_name = 'inventario/inventory_list.html'
    context_object_name = 'entries'
    ordering = ['-date']

class InventoryEntryCreateView(LoginRequiredMixin, InternalUserMixin, CreateView):
    model = ProductReception
    fields = ['product', 'supplier', 'quantity']
    template_name = 'inventario/inventory_form.html'
    success_url = reverse_lazy('inventory_list')
