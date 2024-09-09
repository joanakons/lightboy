from django.urls import path
from orders import views

urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='orders'),
]
