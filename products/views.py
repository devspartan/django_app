from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ProductForm, RawForm
from .models import Products
# Create your views here.


# def product_form_view(request):
#     form = RawForm()
#
#     if request.method == "POST":
#         form = RawForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             my_data = form.cleaned_data
#             Products.objects.create(**my_data)
#
#     context = {
#         'form': form
#     }
#
#     return render(request, "product_form.html", context)

def dynamic_url_routing(request, id):
    obj = Products.objects.get(id=id)
    # obj = get_object_or_404(Products, id=id)
    context = {
        "obj": obj
    }
    return render(request, 'dynamic_url.html', context)


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
    obj_list = Products.objects.all()
    my_context = {
        "object": obj_list
    }
    return render(request, 'product_detail.html', my_context)

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request):
    return render(request, 'about.html', {})