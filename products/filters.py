import django_filters
from django import forms

from products.models import Product


class ProductFilters(django_filters.FilterSet):

    name = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Product Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Search By Product Name"
            }
        )
    )

    brand = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Brand Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Search By Brand Name"
            }
        )
    )

    category = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Category Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Search By Category Name"
            }
        )
    )

    subcategory = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Subcategory Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Search By Subcategory Name"
            }
        )
    )

    price_gte = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Search By Price"
            }
        )
    )

    price_lte = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Search By Price"
            }
        )
    )

    # stock_gte = django_filters.NumberFilter(
    #     field_name='stock',
    #     lookup_expr='gte',
    #     widget=forms.NumberInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': "Search By Stock"
    #         }
    #     )
    # )
    #
    # stock_lte = django_filters.NumberFilter(
    #     field_name='stock',
    #     lookup_expr='lte',
    #     widget=forms.NumberInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': "Search By Stock"
    #         }
    #     )
    # )

    class Meta:
        model = Product
        fields = [
            'name',
            'brand',
            'category',
            'subcategory',
            'price_gte',
            'price_lte',
            # 'stock_gte',
            # 'stock_lte',
            # 'active'
        ]
