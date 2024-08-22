# import re
#
# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from django.core.exceptions import ValidationError
# from account.models import Account
#
#
#
#
# class CustomLoginForm(AuthenticationForm):
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Email'
#             }
#         )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Password'
#             }
#         )
#     )
#
#
# class AccountForm(forms.ModelForm):
#
#     password_confirm = forms.CharField(
#         label="Password confirmation",
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Please confirm your password'
#             }
#         ),
#         help_text=None,  # Remove help text
#     )
#
#     class Meta:
#         model = Account
#         fields = ['first_name', 'last_name', 'email', 'password']
#
#         widgets = {
#             'first_name': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Please enter your first name'
#                 }
#             ),
#             'last_name': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Please enter your last name'
#                 }
#             ),
#             'email': forms.EmailInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Please enter your email'
#                 }
#             ),
#             'password': forms.PasswordInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Please enter your password'
#                 }
#             )
#         }
#
#
#
#     def clean(self):
#         cleaned_data = self.cleaned_data
#
#         if Account.objects.filter(email=cleaned_data.get('email')):
#             self.add_error('email', 'Email address already registered!')
#
#         password = cleaned_data.get("password")
#         password_confirm = cleaned_data.get("password_confirm")
#         password_pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
#
#         if not re.match(password_pattern, password):
#             self.add_error(
#                 'password',
#                 '''Password must be at least 8 characters long,
#                 contain at least one uppercase letter,
#                 one digit, and one special character!''')
#
#         if password and password_confirm:
#             if password != password_confirm:
#                 self.add_error('password_confirm', 'Passwords must match!')
#
#         return cleaned_data
#



from django import forms
from django.contrib.auth.models import User

from account.models import Account


class AccountCreateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'address', 'phone_number',   ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        if User.objects.filter(email=cleaned_data.get('email')):
            self.add_error('email', 'Email already registered!')
        return cleaned_data









