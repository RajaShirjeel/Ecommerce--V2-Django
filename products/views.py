from dal import autocomplete
from django.shortcuts import render, redirect
from .forms import ProductCreationForm, ProductImageForm
from .models import Product
from django.http import JsonResponse
import json

# Create your views here.
def create_product(request):
    if request.method == 'POST':
        product_form = ProductCreationForm(request.POST)
        if product_form.is_valid():
            product_form.save()
    else:
        product_form = ProductCreationForm()
    
    return render(request, 'products/add_products.html', {'form': product_form})


# attach images to the product
def create_product_images(request):
    if request.method == 'POST':
        image_form = ProductImageForm(request.POST, request.FILES)

        if image_form.is_valid():
            image_form.save()

    else:
        image_form = ProductImageForm()
    return render(request, 'products/add_images.html', {'form': image_form})


# send product suggestion to user while typing
def send_products(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query', '')
        result = Product.objects.filter(name__icontains=query)
        products = [product.name for product in result]
        if not products or query == '':
            return JsonResponse({'products': []})
        return JsonResponse({'products': products})

    return JsonResponse({'error', 'invalid request'}, response=400)