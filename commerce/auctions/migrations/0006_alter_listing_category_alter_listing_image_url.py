# Generated by Django 4.1.2 on 2022-10-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_rename_owner_listing_user_listing_current_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[(1, 'Apparel and accessories'), (2, 'Auto and parts'), (3, 'Book, music and video'), (4, 'Computer, technology and eletronics'), (5, 'Furniture'), (6, 'Health, personal care and beauty'), (7, 'Office'), (8, 'Toys and hobby'), (9, 'Other')], default=None, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.CharField(max_length=256, null=True),
        ),
    ]