from django.shortcuts import render

# Create your views here.
from webapp.models import Product


def index_view(request):
    products = Product.objects.order_by("category")
    context = {"products": products}
    return render(request, "index.html", context)
