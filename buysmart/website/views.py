from django.shortcuts import render
from django.http import HttpResponse
from .models import Supermercados
from .models import Carnes
from .models import Vegetales
from .models import Despensa

# Create your views here.


def list_to_queryset(model, data):
    from django.db.models.base import ModelBase

    if not isinstance(model, ModelBase):
        raise ValueError(
            "%s must be Model" % model
        )
    if not isinstance(data, list):
        raise ValueError(
            "%s must be List Object" % data
        )

    pk_list = [obj.pk for obj in data]
    return model.objects

def home_view(request,*args, **kwargs):
    return HttpResponse(render(request, 'index.html'))

def index(request):
    carness = Carnes.objects.all().order_by('precio').order_by('?')
    vegetaless = Vegetales.objects.all().order_by('precio').order_by('?')
    despensass = Despensa.objects.all().order_by('precio').order_by('?')
    supermercados = Supermercados.objects.all()
    if request.method == 'POST':
        pass
    else:
        return render(request, 'index.html', {'carness': carness, 'vegetaless': vegetaless, 'despensass': despensass, 'supermercados': supermercados})


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
    return render(request, 'Groceries.html', {'despensass': despensass, 'supermercados': supermercados})


def Meat(request):
    carness = Carnes.objects.all().order_by('precio')
    supermercados = Supermercados.objects.all()
    return render(request, 'Meat.html', {'carness': carness, 'supermercados': supermercados})


def Meats(request):
    carness = Carnes.objects.all().order_by('precio')
    supermercados = Supermercados.objects.all()
    return render(request, 'Meat.html', {'carness': carness})


def product_single(request):
    if request.method == "POST":
        searched = request.POST['searched']
        try:
            product_01 = Carnes.objects.filter(
                producto__contains=searched).order_by('precio')
            product_02 = Vegetales.objects.filter(
                producto__contains=searched).order_by('precio')
            product_03 = Despensa.objects.filter(
                producto__contains=searched).order_by('precio')
        except:
            searched = "Producto no encontrado"
        return render(request, 'product-single.html', {'searched': searched, 'product_carnes': product_01, 'product_vegetales': product_01, 'product_despensa': product_03})

    else:
        return render(request, 'product-single.html', {})

    #    carness = Carnes.objects.all()
    #    vegetaless = Vegetales.objects.all()
    #    despensas = Despensa.objects.all()
    #    supermercados = Supermercados.objects.all()


def shop(request):
    carness = Carnes.objects.all().order_by('precio')
    vegetaless = Vegetales.objects.all().order_by('precio')
    despensass = Despensa.objects.all().order_by('precio')
    supermercados = Supermercados.objects.all()
    return render(request, 'shop.html', {'carness': carness, 'vegetaless': vegetaless, 'despensass': despensass, 'supermercados': supermercados})


def Vegetables(request):
    vegetaless = Vegetales.objects.all().order_by('precio')
    supermercados = Supermercados.objects.all()
    return render(request, 'Vegetables.html', {'vegetaless': vegetaless, 'supermercados': supermercados})


def wishlist(request):
    return render(request, 'wishlist.html', {})


def test(request):
    carness = Carnes.objects.all().order_by('precio')
    supermercados = Supermercados.objects.all()
    return render(request, 'test.html', {'carness': carness, 'supermercados': supermercados})
