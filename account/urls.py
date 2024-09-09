from django.urls import path
from account import views

urlpatterns = [
    path('sign_up/', views.AccountCreateView.as_view(), name='sign_up'),
    # path('login/', views.CustomLoginView.as_view(), name='login')
    path('account_area/<int:pk>', views.AccountAreaView.as_view(), name='account_area')
]
