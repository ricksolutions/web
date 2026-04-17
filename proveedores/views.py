from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Supplier

class InternalUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_internal()

class SupplierListView(LoginRequiredMixin, InternalUserMixin, ListView):
    model = Supplier
    template_name = 'proveedores/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierCreateView(LoginRequiredMixin, InternalUserMixin, CreateView):
    model = Supplier
    fields = ['name', 'phone', 'email']
    template_name = 'proveedores/supplier_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(LoginRequiredMixin, InternalUserMixin, UpdateView):
    model = Supplier
    fields = ['name', 'phone', 'email']
    template_name = 'proveedores/supplier_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(LoginRequiredMixin, InternalUserMixin, DeleteView):
    model = Supplier
    template_name = 'proveedores/supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')
