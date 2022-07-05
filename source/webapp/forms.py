from django import forms

CATEGORY_CHOICES = [('other', 'Разное'), ('Milk', 'Молоко'), ('Juce', 'Сок'), ('Bread', 'Хлеб')]


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    description = forms.CharField(max_length=2000, label="Description")
    category = forms.ChoiceField(choices = CATEGORY_CHOICES)
    remains = forms.IntegerField(label="Remains")
    price = forms.DecimalField(max_digits=7, decimal_places=2, label="Price")
