from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.db import transaction

from account.models import Account
from orders.models import OrderItem, Order
from products.filters import ProductFilters
from .forms import AddCategoryForm, AddSubcategoryForm, AddProductForm
from .models import Category, Subcategory, Product, ItemInWishlist, ItemInCart


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


# class UpdateProductView(LoginRequiredMixin, UpdateView):
#     template_name = 'student/update_student.html'
#     model = Student
#     form_class = StudentUpdateForm
#     success_url = reverse_lazy('list-of-students')


class ProductListView(ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 20  # Number of items per page

    def get_queryset(self):
        products = Product.objects.filter(active=True)
        my_filters = ProductFilters(self.request.GET, queryset=products)
        return my_filters.qs
        # return Product.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = self.get_queryset()
        # products = Product.objects.filter(active=True)
        my_filters = ProductFilters(self.request.GET, queryset=products)
        filtered_products = my_filters.qs

        # Paginate the filtered products
        paginator = Paginator(filtered_products, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Update context to use paginated products
        context['all_products'] = page_obj
        context['filters_form'] = my_filters.form
        # list_of_ids = [item.product.id for item in ItemInWishlist.objects.filter(user_id=self.request.user.id)]
        # context['list_of_ids'] = list_of_ids

        if self.request.user.is_authenticated:
            user_cart_items = ItemInCart.objects.filter(user=self.request.user)
            user_wishlist_items = ItemInWishlist.objects.filter(user=self.request.user)

            cart_product_ids = set(user_cart_items.values_list('product_id', flat=True))
            wishlist_product_ids = set(user_wishlist_items.values_list('product_id', flat=True))

            # Attach cart_status and wishlist_status to each product instance
            for product in filtered_products:
                product.cart_status = product.id in cart_product_ids
                product.wishlist_status = product.id in wishlist_product_ids
        else:
            # Set default status for unauthenticated users
            for product in filtered_products:
                product.cart_status = False
                product.wishlist_status = False

        return context


class ProductOnSaleListView(ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_sale=True, active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = self.get_queryset()
        my_filters = ProductFilters(self.request.GET, queryset=products)
        filtered_products = my_filters.qs
        context['all_products'] = filtered_products
        context['filters_form'] = my_filters.form

        cart_status = {}
        wishlist_status = {}

        if self.request.user.is_authenticated:
            user_cart_items = ItemInCart.objects.filter(user=self.request.user)
            user_wishlist_items = ItemInWishlist.objects.filter(user=self.request.user)

            cart_product_ids = set(user_cart_items.values_list('product_id', flat=True))
            wishlist_product_ids = set(user_wishlist_items.values_list('product_id', flat=True))

            for product in filtered_products:
                cart_status[product.id] = product.id in cart_product_ids
                wishlist_status[product.id] = product.id in wishlist_product_ids

        context['cart_status'] = cart_status
        context['wishlist_status'] = wishlist_status

        return context


class ProductView(DetailView):
    template_name = 'products/product.html'
    model = Product


@login_required
def add_to_wishlist(request, pk):
    if ItemInWishlist.objects.filter(product_id=pk, user__id=request.user.id).exists() is False:
        new_item = ItemInWishlist()
        new_item.user = Account.objects.get(id=request.user.id)
        new_item.product_id = pk
        new_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_from_wishlist(request, pk):
    item_to_delete = get_object_or_404(ItemInWishlist, user=request.user, product_id=pk)
    item_to_delete.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class WishListView(LoginRequiredMixin, ListView):
    model = ItemInWishlist
    template_name = 'products/wishlist.html'
    context_object_name = 'wishlist'

    def get_queryset(self):
        # Get the wishlist for the logged-in user
        return ItemInWishlist.objects.filter(user=self.request.user)


@login_required
def add_to_cart(request, pk):
    print(pk, 'tralala')
    if ItemInCart.objects.filter(product_id=pk, user__id=request.user.id, active=True).exists() is False:
        new_item = ItemInCart()
        new_item.user = Account.objects.get(id=request.user.id)
        new_item.product_id = pk

        # Add the item to the cart
        new_item.save()
    else:
        item_instance = ItemInCart.objects.get(product_id=pk, user__id=request.user.id, active=True)
        item_instance.quantity += 1
        item_instance.save()

    # Redirect back to the previous page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart_item_increment(request, pk):
    item_instance = ItemInCart.objects.get(product_id=pk, user__id=request.user.id, active=True)
    # .last se asigura ca ia ultimul item din query, sau .first primul
    # ItemInCart.objects.filter(product_id=pk, user__id=request.user.id, active=True).last()
    item_instance.quantity += 1
    item_instance.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart_item_decrement(request, pk):
    item_instance = ItemInCart.objects.get(product_id=pk, user__id=request.user.id, active=True)
    item_instance.quantity -= 1

    if item_instance.quantity == 0:
        item_instance.quantity = 1

    item_instance.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def update_quantity_in_cart(request, pk):
    user = Account.objects.get(id=request.user.id)

    try:
        # Try to get the item in the cart
        item_in_cart = ItemInCart.objects.get(user=user, product_id=pk)
        # Increment the quantity if the item exists
        item_in_cart.quantity += 1
        item_in_cart.save()
    except ItemInCart.DoesNotExist:
        new_item = ItemInCart()
        new_item.user = user
        new_item.product_id = pk

        # Add the item to the cart
        new_item.save()

    # Redirect back to the previous page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_from_cart(request, pk):
    # Get the item from the cart for the current user and the given product ID
    item_to_delete = get_object_or_404(ItemInCart, user=request.user, product=pk)

    # Delete the item from the cart
    item_to_delete.delete()

    # Redirect back to the previous page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CartView(LoginRequiredMixin, ListView):
    model = ItemInCart
    template_name = 'products/cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return ItemInCart.objects.filter(user=self.request.user, active=True)

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        price_per_item = []
        total_cart = 0

        for item in ItemInCart.objects.filter(user=self.request.user, active=True):
            total_cart += item.quantity * item.product.price
            new_total = item.product.price * item.quantity
            price_per_item.append(new_total)
        context['total_cart'] = total_cart
        context['price_per_item'] = price_per_item
        return context


@login_required
def create_order(request):
    cart = ItemInCart.objects.filter(user=request.user, active=True)
    user = Account.objects.get(id=request.user.id)

    if cart.exists():
        # with transaction.atomic():  # Start a transaction

        new_order = Order.objects.create(user=user)

        for item in cart:
            price = item.product.price

            if item.product.is_sale:
                price = item.product.sale_price

            OrderItem.objects.create(
                order=new_order,
                product=item.product,
                price=price,
                quantity=item.quantity,
            )

            product = Product.objects.get(id=item.product.id)
            product.stock -= item.quantity
            product.save()

            item.active = False
            item.save()

    return redirect('home')  # TODO: Add order success page instead of home
# def create_order(request, pk):
#     cart = []
#     if request.user.is_authenticated:
#         cart = ItemInCart.objects.filter(user=request.user)
#
#     if cart is not None and len(cart) > 0:
#         new_order = Order()
#         new_order.user = Account.objects.get(id=request.user.id)
#         new_order.save()
#
#         for item in cart:
#             new_order_item = OrderItem()
#             new_order_item.order = new_order
#             new_order_item.product_id = pk
#             new_order_item.price = item.product.price
#             new_order_item.save()
#             item.is_active = False
#             item.save()
#
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     # Initialize flags as False
#     item_in_cart = False
#     item_in_wishlist = False
#
#     # Ensure the user is authenticated before making queries
#     if request.user.is_authenticated:
#         item_in_cart = ItemInCart.objects.filter(
#             user=request.user,
#             product=product
#         ).exists()
#         item_in_wishlist = ItemInWishlist.objects.filter(
#             user=request.user,
#             product=product
#         ).exists()
#
#     context = {
#         'product': product,
#         'item_in_cart': item_in_cart,
#         'item_in_wishlist': item_in_wishlist,
#     }
#
#     return render(request, 'products/product.html', context)
#
#
# def product_list(request):
#     products = Product.objects.all()
#
#     cart_status = {}
#     wishlist_status = {}
#
#     if request.user.is_authenticated:
#         user_cart_items = ItemInCart.objects.filter(user=request.user)
#         user_wishlist_items = ItemInWishlist.objects.filter(user=request.user)
#
#         cart_product_ids = set(user_cart_items.values_list('product_id', flat=True))
#         wishlist_product_ids = set(user_wishlist_items.values_list('product_id', flat=True))
#
#         for product in products:
#             cart_status[product.id] = product.id in cart_product_ids
#             wishlist_status[product.id] = product.id in wishlist_product_ids
#
#     context = {
#         'products': products,
#         'cart_status': cart_status,
#         'wishlist_status': wishlist_status,
#     }
#
#     return render(request, 'products/product_list.html', context)

# indoor - subcategories html
# configurator - form: enter room dimensions length, width, height, choose from: bedroom, living room, kitchen, childrens room, bathroom, hallway, office
# calculate necessa
