from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django import forms
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import User

class DashboardHomeView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard_home.html'

    def test_func(self):
        return self.request.user.is_internal()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from productos.models import Product
        from proveedores.models import Supplier
        context['total_products'] = Product.objects.count()
        context['total_suppliers'] = Supplier.objects.count()
        context['total_stock'] = sum([p.stock for p in Product.objects.all()])
        return context


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('store_home')
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    
    def get_success_url(self):
        user = self.request.user
        if user.is_internal():
            return reverse_lazy('dashboard_home')
        return reverse_lazy('store_home')
