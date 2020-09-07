from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm
from .models import Products
# Create your views here.

def product_form_view(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, "product_form.html", context)

def product_view(request, *args, **kwargs):
    obj = Products.objects.get(id=1)

    my_context = {
        "object": obj
    }
    return render(request, 'product_detail.html', my_context)

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request):
    return render(request, 'about.html', {})