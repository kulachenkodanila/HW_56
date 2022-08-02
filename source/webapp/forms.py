from django import forms

from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "remains", "price"]


class UserProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "remains", "price"]