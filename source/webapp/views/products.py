from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from webapp.forms import ProductForm, UserProductForm
from webapp.models import Product


class IndexView(ListView):
    model = Product
    template_name = "products/index.html"
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.all()


class ProductView(DetailView):
    template_name = "products/product_view.html"
    model = Product


class DeleteProduct(DeleteView):
    model = Product

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("index")


class CreateProduct(CreateView):
    form_class = ProductForm
    template_name = "products/product_create.html"

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        form.save_m2m()
        return redirect("product_view", pk=product.pk)


class UpdateProduct(UpdateView):
    form_class = ProductForm
    template_name = "products/product_update.html"
    model = Product

    def get_form_class(self):
        if self.request.GET.get("is_admin"):
            return ProductForm
        return UserProductForm

    def get_success_url(self):
        return reverse("product_view", kwargs={"pk": self.object.pk})

