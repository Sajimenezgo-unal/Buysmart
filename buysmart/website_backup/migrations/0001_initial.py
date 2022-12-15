# Generated by Django 4.0 on 2022-11-05 18:20

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Supermercados',
            fields=[
                ('supermercado_id', models.AutoField(db_column='Supermercado_id', primary_key=True, serialize=False)),
                ('nombre', models.TextField(blank=True, db_column='Nombre', null=True)),
            ],
            options={
                'db_table': 'Supermercados',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Vegetales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.TextField(blank=True, db_column='Producto', null=True)),
                ('precio', models.TextField(blank=True, db_column='Precio', null=True)),
                ('imagen_url', models.TextField(blank=True, db_column='Imagen_url', null=True)),
                ('url', models.TextField(blank=True, db_column='Url', null=True)),
                ('supermercado', models.ForeignKey(blank=True, db_column='Supermercado_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.supermercados')),
            ],
            options={
                'db_table': 'Vegetales',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Despensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.TextField(blank=True, db_column='Producto', null=True)),
                ('precio', models.TextField(blank=True, db_column='Precio', null=True)),
                ('imagen_url', models.TextField(blank=True, db_column='Imagen_url', null=True)),
                ('url', models.TextField(blank=True, db_column='Url', null=True)),
                ('supermercado', models.ForeignKey(blank=True, db_column='Supermercado_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.supermercados')),
            ],
            options={
                'db_table': 'Despensa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Carnes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.TextField(blank=True, db_column='Producto', null=True)),
                ('precio', models.FloatField(blank=True, db_column='Precio', null=True)),
                ('imagen_url', models.TextField(blank=True, db_column='Imagen_url', null=True)),
                ('url', models.TextField(blank=True, db_column='Url', null=True)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='producto')),
                ('supermercado', models.ForeignKey(blank=True, db_column='Supermercado_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.supermercados')),
            ],
            options={
                'db_table': 'Carnes',
                'managed': True,
            },
        ),
    ]