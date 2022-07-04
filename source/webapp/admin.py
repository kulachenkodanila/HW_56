from django.contrib import admin

# Register your models here.
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'remains', 'price']
    list_display_links = ['name']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['name', 'description', 'category', 'remains', 'price']
    readonly_fields = []


admin.site.register(Product, ProductAdmin)