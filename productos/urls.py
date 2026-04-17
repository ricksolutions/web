from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, export_products_excel

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('export/', export_products_excel, name='export_products'),
]
