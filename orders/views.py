from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import render
from orders.models import Order, OrderItem


class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'orders/orders_list.html'
    model = Order
    context_object_name = 'order'

    def get_queryset(self):
        # Filter the queryset to only include the logged-in user's account
        return Order.objects.filter()

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        orders = Order.objects.filter()

        items = []

        for order in orders:
            items = OrderItem.objects.filter(order=order.id)

        # for item in ItemInCart.objects.filter(user=self.request.user, active=True):
        #     total_cart += item.quantity * item.product.price
        #     new_total = item.product.price * item.quantity
        #     price_per_item.append(new_total)
        # context['items'] = total_cart
        context['order_items'] = items
        return context


class OrderDetailView(LoginRequiredMixin, DetailView):
    template_name = 'account/order_detail.html'
    context_object_name = 'order_detail'
    model = OrderItem

    def get_queryset(self):
        return OrderItem.objects.filter(user=self.request.user, active=True)


def get_user_orders(request):
    # Assuming the user is authenticated and you have a `user` field on the `Order` model
    user = request.user

    # Filter orders by the authenticated user
    orders = Order.objects.filter(user=user).annotate(
        item_count=Count('items')
    )

    # Calculate the total price for each order
    for order in orders:
        order.total_price = order.get_total()

    return {
        'all_orders': orders
    }

#     def get_context_data(self, **kwargs):
#         context = super(OrderDetailView, self).get_context_data(**kwargs)

# def my_account_view(request):
#     order_detail = OrderDetail.objects.filter(user=request.user).first()
#     if not order_detail:
#         # Handle the case where no order detail exists
#         return render(request, 'account_area.html', {
#             'account_id': request.user.id,
#             'order_detail': None
#         })
#     return render(request, 'account_area.html', {
#         'account_id': request.user.id,
#         'order_detail': order_detail
#     })



# class UserOrderView(LoginRequiredMixin, ListView):
#     template_name = 'account/my_orders.html'
#     context_object_name = 'my_orders'
#     model = OrderItem
# def get_all_user_orders(request, pk):
#     if request.user.is_authenticated:
#         user_orders = Order.objects.filter(user=request.user)
#     else:
#         user_orders = Order.objects.none()  # Empty queryset if not logged in
#
#     return {
#         'my_orders': user_orders
#     }