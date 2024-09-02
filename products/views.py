from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from products.filters import ProductFilters
from .forms import AddCategoryForm, AddSubcategoryForm, AddProductForm
from .models import Category, Subcategory, Product


class AddCategory(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'products/add_category.html'
    form_class = AddCategoryForm
    success_url = reverse_lazy('home')


class AddSubcategory(LoginRequiredMixin, CreateView):
    model = Subcategory
    template_name = 'products/add_subcategory.html'
    form_class = AddSubcategoryForm
    success_url = reverse_lazy('home')


class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/add_product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('home')


class ProductListView(ListView):
    template_name = 'products/products.html'
    model = Product
    # context_object_name = Product.objects.all()
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = Product.objects.filter(active=True)
        my_filters = ProductFilters(self.request.GET, queryset=products)
        context['all_products'] = my_filters.qs
        context['filters_form'] = my_filters.form

        return context


class ProductView(DetailView):
    template_name = 'products/product.html'
    model = Product



# indoor - subcategories html
# configurator - form: enter room dimensions length, width, height, choose from: bedroom, living room, kitchen, childrens room, bathroom, hallway, office
# calculate necessa



