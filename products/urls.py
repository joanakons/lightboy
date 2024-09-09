from django.urls import path
# from .views import category_view
from products import views

urlpatterns = [
    # path('categories/', views.CategoryView.as, name='category_view'),
    path('add_category/', views.AddCategory.as_view(), name='add_category'),
    path('add_subcategory/', views.AddSubcategory.as_view(), name='add_subcategory'),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products-on-sale/', views.ProductOnSaleListView.as_view(), name='products-on-sale'),
    path('product/<int:pk>/', views.ProductView.as_view(), name='product'),
    path('wishlist/', views.WishListView.as_view(), name='wishlist'),
    path('add_to_wishlist/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete_from_wishlist/<int:pk>/', views.delete_from_wishlist, name='delete_from_wishlist'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('update_quantity_in_cart/<int:pk>/', views.update_quantity_in_cart, name='update_quantity_in_cart'),
    path('delete_from_cart/<int:pk>/', views.delete_from_cart, name='delete_from_cart'),
    path('cart_item_increment/<int:pk>/', views.cart_item_increment, name='cart_item_increment'),
    path('cart_item_decrement/<int:pk>/', views.cart_item_decrement, name='cart_item_decrement'),
    path('create_order/', views.create_order, name='create_order'),
    # path('user_orders/', views.user_orders, name='create_order'),
]
