from django.shortcuts import render
from .models import Supermercados
from .models import Carnes
from .models import Vegetales
from .models import Despensa

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def blog_single(request):
    return render(request, 'blog-single.html', {})


def cart(request):
    return render(request, 'cart.html', {})


def checkout(request):
    return render(request, 'checkout.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def Groceries(request):
    despensass = Despensa.objects.all().order_by('precio')
    supermercados = Supermercados.objects.all()
    return render(request, 'Groceries.html', {'despensass':despensass,'supermercados':supermercados})


def Meat(request):
    carness = Carnes.objects.all().order_by('precio')
    supermercados = Supermercados.objects.all()
    return render(request, 'Meat.html',{'carness':carness,'supermercados':supermercados})

def Meats(request):
    carness = Carnes.objects.all().order_by('precio')
    supermercados = Supermercados.objects.all()
    return render(request, 'Meat.html',{'carness':carness})


def product_single(request):
    carness = Carnes.objects.all()
    vegetaless = Vegetales.objects.all()
    despensas = Despensa.objects.all()
    supermercados = Supermercados.objects.all()
    return render(request, 'product-single.html', {'carness':carness,'vegetaless':vegetaless,'despensas':despensas,'supermercados':supermercados})

def shop(request):
    carness = Carnes.objects.all()
    vegetaless = Vegetales.objects.all()
    despensass = Despensa.objects.all()
    supermercados = Supermercados.objects.all()
    return render(request, 'shop.html', {'carness':carness,'vegetaless':vegetaless,'despensass':despensass,'supermercados':supermercados})


def Vegetables(request):
    vegetaless = Vegetales.objects.all().order_by('precio')
    supermercados = Supermercados.objects.all()
    return render(request, 'Vegetables.html', {'vegetaless':vegetaless, 'supermercados':supermercados})


def wishlist(request):
    return render(request, 'wishlist.html', {})

def test(request):
    carness = Carnes.objects.all().order_by('precio')
    supermercados = Supermercados.objects.all()
    return render(request, 'test.html', {'carness':carness, 'supermercados':supermercados})


