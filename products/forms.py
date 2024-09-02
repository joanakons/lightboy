from django import forms

from products.models import Product, Category, Subcategory

FORMS_MODEL_CHOICE_FIELD = forms.ModelChoiceField(
    queryset=Category.objects.all(),
    widget=forms.Select(attrs={'class': 'form-control'}),
    empty_label="Select Category"  # Optional placeholder
)


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'brand', 'category', 'price', 'stock', 'added_at']

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please Enter a Category Name'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please Enter a Category Description'
                }
            )
        }


class AddSubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'description', 'parent']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please Enter a Subcategory Name'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please Enter a Subcategory Description'
                }
            ),
            'parent': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }

        parent = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            empty_label="Select Category"  # Optional placeholder
        )


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'brand',
            'category',
            'subcategory',
            'image',
            'image2',
            'image3',
            'price',
            'sale_price',
            'is_sale',
            'stock',
            'active'
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'brand': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image2': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image3': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'subcategory': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sale_price': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'is_sale': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'active': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'type': 'checkbox',
                    'role': 'switch'
                }
            )
        }

        category = FORMS_MODEL_CHOICE_FIELD

        subcategory = forms.ModelChoiceField(
            queryset=Subcategory.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            empty_label="Select Subcategory"  # Optional placeholder
        )

        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': ''
        #         }),
        #     'last_name': forms.TextInput(
        #         attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
        #     'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
        #     'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your address'}),
        #     'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number'}),
        # }
