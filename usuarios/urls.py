from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, CustomLoginView, DashboardHomeView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register, name='register'),
    path('dashboard/', DashboardHomeView.as_view(), name='dashboard_home'),
]

