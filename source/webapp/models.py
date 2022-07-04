from django.core.validators import MinValueValidator
from django.db import models

CATEGORY_CHOICES = [('other', 'Разное'), ('Milk', 'Молоко'), ('Juce', 'Сок'), ('Bread', 'Хлеб')]
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(max_length=2000, verbose_name="Описание")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                              verbose_name="Категория")
    remains = models.IntegerField( verbose_name="Остаток")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")


    def __str__(self):
        return f"{self.id}. {self.name}: {self.category}"

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"