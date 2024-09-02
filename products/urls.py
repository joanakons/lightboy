from django.urls import path
# from .views import category_view
from products import views

urlpatterns = [
    # path('categories/', views.CategoryView.as, name='category_view'),
    path('add_category/', views.AddCategory.as_view(), name='add_category'),
    path('add_subcategory/', views.AddSubcategory.as_view(), name='add_subcategory'),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>/', views.ProductView.as_view(), name='product')
]
