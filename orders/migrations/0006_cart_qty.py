# Generated by Django 3.0.7 on 2020-07-09 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_cart_subadditional'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
