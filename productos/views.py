from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from proveedores.views import InternalUserMixin # reuse the mixin
from .models import Product
import openpyxl

class ProductListView(LoginRequiredMixin, InternalUserMixin, ListView):
    model = Product
    template_name = 'productos/product_list.html'
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, InternalUserMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'stock', 'image']
    template_name = 'productos/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(LoginRequiredMixin, InternalUserMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'stock', 'image']
    template_name = 'productos/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(LoginRequiredMixin, InternalUserMixin, DeleteView):
    model = Product
    template_name = 'productos/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

def export_products_excel(request):
    if not (request.user.is_authenticated and request.user.is_internal()):
        return HttpResponse('Unauthorized', status=401)
    
    products = Product.objects.all()
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Products'

    # Headers
    headers = ['ID', 'Name', 'Description', 'Price', 'Stock']
    sheet.append(headers)

    for product in products:
        sheet.append([product.id, product.name, product.description, float(product.price), product.stock])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="inventory_products.xlsx"'
    workbook.save(response)
    return response

