from django.forms import FloatField
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Count, F, Case, When, DecimalField, ExpressionWrapper
from products.models import Category, Subcategory, ItemInCart, ItemInWishlist
from orders.models import Order, OrderItem


def get_all_categories(request):
    categories = Category.objects.all()

    list_categories_with_subcategories = []
    for category in categories:
        if Subcategory.objects.filter(parent=category).exists():
            list_categories_with_subcategories.append(category.id)
    return {'categories': categories,
            'list_active_categories': list_categories_with_subcategories
            }


def get_all_subcategories(request):
    subcategories = Subcategory.objects.all()
    return {'subcategories': subcategories}


# lista cu id urile categoriilor care au subcategorie


def subcategories_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    category_dict = category.get_subcategories_dict()
    print(category_dict)  # Debugging: Check if this is populated correctly
    return {'category_dict': category_dict}


def get_all_cart_items(request):
    cart = []
    if request.user.is_authenticated:
        cart = ItemInCart.objects.filter(user=request.user, active=True)

    return {
        'cart_items': cart,
    }


def get_all_orders(request):
    orders = Order.objects.filter().annotate(
        item_count=Count('items')
    )

    for order in orders:
        order.total_price = order.get_total()

    return {
        'all_orders': orders
    }


def get_all_user_orders(request):
    orders = []
    if request.user.is_authenticated:
        orders = Order.objects.filter(user_id=request.user.id)

    for order in orders:
        order_items = OrderItem.objects.filter(order=order).values_list('quantity', flat=True)
        order.item_count = len(order_items)
        order.total_price = order.get_total()

    return {
        'user_orders': orders
    }

    # Calculate total price considering sale prices
    #     total_price = cart.aggregate(
    #         total=Sum(
    #             Case(
    #                 When(product__is_sale=True, then=F('product__sale_price') * F('quantity')),
    #                 default=F('product__price') * F('quantity'),
    #                 output_field=DecimalField()
    #             )
    #         )
    #     )['total'] or 0
    #
    #     sub_total_price = cart.aggregate(
    #         total=Sum(
    #             Case(
    #                 When(product__is_sale=True, then=F('product__sale_price') * F('quantity')),
    #                 default=F('product__price') * F('quantity'),
    #                 output_field=DecimalField()
    #             )
    #         )
    #     )['total'] or 0  # If the cart is empty, total should be 0
    # else:
    #     cart = ItemInCart.objects.none()  # Empty queryset if not logged in
    #     total_price = 0


def get_all_wishlist_items(request):
    if request.user.is_authenticated:
        wishlist = ItemInWishlist.objects.filter(user=request.user)
    else:
        wishlist = ItemInWishlist.objects.none()  # Empty queryset if not logged in
    return {
        'wishlist_items': wishlist,
    }
