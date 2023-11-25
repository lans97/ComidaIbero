from django.db import models
from django.contrib.auth.models import User

class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.TextField()
    descripcion = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_unitario = models.FloatField()
    is_topping = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1)
    registration_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def precio_total(self):
        suma = 0
        for orden_item in self.ordenitem_set.all():
            suma += orden_item.producto.precio_unitario
        return suma

    def items_str(self):
        ordered_items = self.ordenitem_set.order_by('parentItem', 'numItem')
        desc = ", ".join(str(item) for item in ordered_items)
        desc = desc[:-1]
        return desc

    def __str__(self):
        return f"Orden #{self.pk} - Para: {self.usuario.username}"

class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    numItem = models.IntegerField()
    parentItem = models.IntegerField(default=0)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        desc = ""
        if self.producto.is_topping:
            desc += "{}\t\t{:.02f}".format(self.producto.nombre, self.producto.precio_unitario)
        else:
            desc += "{}\t{:.02f}".format(self.producto.nombre, self.producto.precio_unitario)
        return desc
