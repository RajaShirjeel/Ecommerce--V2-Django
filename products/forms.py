from django import forms
from django.forms import ModelForm
from .models import Product, ProductImage

class ProductCreationForm(ModelForm):
    class Meta: 
        model = Product
        fields = ["name", "price", "description", "category", "colors", "sizes"]
        labels = {
            'name': 'Product Name:',
            'price': 'Product Price:',
            'description': 'Product Description: ',
            'category': 'Category:',
            'colors': 'Product colors:',
            'sizes': 'Product sizes:'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'create-product-inputs'}),
            'price': forms.NumberInput(attrs={'class': 'create-product-inputs'}),
            'description': forms.TextInput(attrs={'class': 'create-product-inputs'}),
            'category': forms.Select(attrs={'class': 'create-product-slides'}),
            'colors': forms.SelectMultiple(attrs={'class': 'create-product-slides'}),
            'sizes': forms.SelectMultiple(attrs={'class': 'create-product-slides'})
        }


class ProductImageForm(ModelForm):
    class Meta: 
        model = ProductImage
        fields = ['image', 'product']
        labels = {
            'product': 'name of product',
        }

    product = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Start typing to search...', 'class': 'add-product-input'})
    )

    def clean_product(self):
        query = self.cleaned_data.get('product')

        try:
            return Product.objects.get(name=query)
        except Product.DoesNotExist:
            raise forms.ValidationError('No product with the name exists')