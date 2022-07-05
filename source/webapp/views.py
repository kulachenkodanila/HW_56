from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from webapp.forms import ProductForm
from webapp.models import Product


def index_view(request):
    products = Product.objects.order_by("category")
    context = {"products": products}
    return render(request, "index.html", context)


def product_view(request, **kwargs):
    pk = kwargs.get("pk")
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_view.html", {"product": product})


def create_product(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "create.html", {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            description = form.cleaned_data.get("description")
            category = form.cleaned_data.get("category")
            remains = form.cleaned_data.get("remains")
            price = form.cleaned_data.get("price")
            new_product = Product.objects.create(name=name, description=description, category=category, remains=remains,
                                                 price=price)
            return redirect("product_view", pk=new_product.pk)
        return render(request, "create.html", {"form": form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {"product": product})
    else:
        product.delete()
        return redirect("index")


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(initial={
            "name": product.name,
            "description": product.description,
            "category": product.category,
            "remains": product.remains,
            "price": product.price,
        })
        return render(request, "update.html", {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get("name")
            product.description = form.cleaned_data.get("description")
            product.category = form.cleaned_data.get("category")
            product.remains = form.cleaned_data.get("remains")
            product.price = form.cleaned_data.get("price")
            product.save()
            return redirect("index")
        return render(request, "update.html", {"form": form})
