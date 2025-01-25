from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('create-new-product', views.create_product, name='create_product'),
    path('create-product-image', views.create_product_images, name='create_product_image'),
    path('send-products', views.send_products, name='send_products')
]