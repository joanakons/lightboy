from django.shortcuts import get_object_or_404

from products.models import Category, Subcategory


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




