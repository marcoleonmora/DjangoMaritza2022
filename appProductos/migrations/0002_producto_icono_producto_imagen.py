# Generated by Django 4.1.2 on 2022-10-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProductos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='icono',
            field=models.ImageField(null=True, upload_to='iconos'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
