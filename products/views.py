from dal import autocomplete
from django.shortcuts import render, redirect
from .forms import ProductCreationForm, ProductImageForm
from .models import Product

# Create your views here.
def create_product(request):
    if request.method == 'POST':
        product_form = ProductCreationForm(request.POST)
        if product_form.is_valid():
            product_form.save()
        else:
            return render(request, 'products/add_products.html')
        return render(request, 'products/add_products.html')
    
    else:
        product_form = ProductCreationForm()
    
    return render(request, 'products/add_products.html', {'form': product_form})


# attach images to the product
def create_product_images(request):
    if request.method == 'POST':
        image_form = ProductImageForm(request.POST, request.FILES)

        if image_form.is_valid():
            image_form.save()
        return render(request, 'products/add_images.html')

    else:
        image_form = ProductImageForm()
    return render(request, 'products/add_images.html', {'form': image_form})

