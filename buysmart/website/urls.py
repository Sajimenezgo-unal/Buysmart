from django import views
from django.urls import path
from .import views

app_name = 'core'

urlpatterns = [
    path('index.html', views.index, name="index"),
    path('about.html', views.about, name="about"),
    path('shop.html', views.shop, name="shop"),
    path('blog-single.html', views.blog_single, name="blog_single"),
    path('blog.html', views.blog, name="blog"),
    path('cart.html', views.cart, name="cart"),
    path('checkout.html', views.checkout, name="checkout"),
    path('contact.html', views.contact, name="contact"),
    path('Groceries.html', views.Groceries, name="Groceries"),
    path('Meat.html', views.Meat, name="Meat"),
    path('product-single.html', views.product_single, name="product_single"),
    path('Vegetables.html', views.Vegetables, name="Vegetables"),
    path('wishlist.html', views.wishlist, name="wishlist"),
    path('test.html', views.test, name="test"),

]
