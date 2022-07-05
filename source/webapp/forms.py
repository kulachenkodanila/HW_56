from django import forms

CATEGORY_CHOICES = [('other', 'Разное'), ('Milk', 'Молоко'), ('Juce', 'Сок'), ('Bread', 'Хлеб')]


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, null=False, blank=False, verbose_name="Name")
    description = forms.TextField(max_length=2000, verbose_name="Description")
    category = forms.CharField(max_length=30, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                               verbose_name="Category")
    remains = forms.IntegerField(verbose_name="Remains")
    price = forms.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price")
