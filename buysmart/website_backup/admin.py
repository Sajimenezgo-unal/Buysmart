from django.contrib import admin

# Register your models here.
from .models import Meat
from .models import Supermercados
from .models import Carnes
from .models import Vegetales
from .models import Despensa

admin.site.register(Meat)
admin.site.register(Supermercados)
admin.site.register(Carnes)
admin.site.register(Vegetales)
admin.site.register(Despensa)