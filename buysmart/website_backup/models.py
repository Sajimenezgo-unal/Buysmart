from django.db import models

# Create your models here.
class Meat(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()

class Supermercados(models.Model):
    supermercado_id = models.AutoField(db_column='Supermercado_id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Supermercados'

class Carnes(models.Model):
    producto = models.TextField(db_column='Producto', blank=True, null=True)  # Field name made lowercase.
    precio = models.FloatField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.
    supermercado = models.ForeignKey('Supermercados', models.DO_NOTHING, db_column='Supermercado_id', blank=True, null=True)  # Field name made lowercase.
    imagen_url = models.TextField(db_column='Imagen_url', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='Url', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Carnes'

class Vegetales(models.Model):
    producto = models.TextField(db_column='Producto', blank=True, null=True)  # Field name made lowercase.
    precio = models.TextField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.
    supermercado = models.ForeignKey('Supermercados', models.DO_NOTHING, db_column='Supermercado_id', blank=True, null=True)  # Field name made lowercase.
    imagen_url = models.TextField(db_column='Imagen_url', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='Url', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Vegetales'


class Despensa(models.Model):
    producto = models.TextField(db_column='Producto', blank=True, null=True)  # Field name made lowercase.
    precio = models.TextField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.
    supermercado = models.ForeignKey('Supermercados', models.DO_NOTHING, db_column='Supermercado_id', blank=True, null=True)  # Field name made lowercase.
    imagen_url = models.TextField(db_column='Imagen_url', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='Url', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Despensa'

