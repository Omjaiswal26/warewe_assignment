# Generated by Django 4.1 on 2023-01-31 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_cart_user_remove_order_order_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(related_name='order_items', to='accounts.cartitems'),
        ),
    ]
