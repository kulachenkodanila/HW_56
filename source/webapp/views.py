from django.shortcuts import render, get_object_or_404

# Create your views here.
from webapp.models import Product


def index_view(request):
    products = Product.objects.order_by("category")
    context = {"products": products}
    return render(request, "index.html", context)


def product_view(request, **kwargs):
    pk = kwargs.get("pk")
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_view.html", {"product": product})
