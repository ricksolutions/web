from django.urls import path
from .views import InventoryEntryListView, InventoryEntryCreateView

urlpatterns = [
    path('', InventoryEntryListView.as_view(), name='inventory_list'),
    path('new/', InventoryEntryCreateView.as_view(), name='inventory_entry'),
]
