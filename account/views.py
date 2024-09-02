import random
import string

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from FinalProject.settings import DEFAULT_FROM_EMAIL
from account.forms import AccountCreateForm
from account.models import Account
from django.core.mail import send_mail

# Create your views here.
class AccountCreateView(SuccessMessageMixin, CreateView):
    template_name = 'account/create_user.html'
    model = Account
    form_class = AccountCreateForm
    success_url = reverse_lazy('login')
    success_message = 'Your account has been created!'

    def get_success_message(self, cleaned_data):
        return self.success_message

    def form_invalid(self, form):
        print(form.errors, "23")

        return super(AccountCreateView, self).form_invalid(form)

    def form_valid(self, form):
        if form.is_valid():
            new_account = form.save(commit=False)
            username = f'{new_account.first_name[0].lower()}_{new_account.last_name.lower()}{random.randint(1000,9999)}'
            # TO DO: verificre unicitate username

            while Account.objects.filter(username=username).exists():
                username = f'{new_account.first_name[0].lower()}_{new_account.last_name.lower()}{random.randint(1000, 9999)}'


            password = ''.join(
                random.SystemRandom().choice(
                    string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
                for _ in range(8))
            print('username:', username, '   password:', password)
            new_account.set_password(password)
            new_account.username = username

            new_subject = 'New Account Added'
            new_message = f' Your username is: {username} ;  Your password is: {password}'
            send_mail(new_subject, new_message, DEFAULT_FROM_EMAIL, [new_account.email])


            new_account.save()

            return super(AccountCreateView, self).form_valid(form)





# import re
# import string
#
# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views import View
# from django.views.generic import CreateView
#
# import random
# from account.forms import AccountForm
# from account.models import Account
# from django.contrib.auth.views import LoginView
# from .forms import CustomLoginForm
#
#
#
# class CustomLoginView(LoginView):
#     form_class = CustomLoginForm
#     template_name = 'registration/login.html'
#
#
# class AccountCreateView(CreateView):
#
#     template_name = 'account/create_user.html'
#     model = Account
#     form_class = AccountForm
#     success_url = reverse_lazy('login')
#
#     def form_valid(self, form):
#         if form.is_valid():
#             new_account = form.save(commit=False)
#
#             return super(AccountCreateView, self).form_valid(form)
#
#     def form_invalid(self, form):
#
#         return super(AccountCreateView, self).form_invalid(form)
#
