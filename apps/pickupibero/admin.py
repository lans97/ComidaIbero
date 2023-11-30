from django.contrib import admin
from .models import Restaurante, Producto, Orden, OrdenItem, RelacionToppings

admin.site.register(Restaurante)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(OrdenItem)
admin.site.register(RelacionToppings)
