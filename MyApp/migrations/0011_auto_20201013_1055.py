# Generated by Django 3.1.1 on 2020-10-13 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_auto_20201010_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
