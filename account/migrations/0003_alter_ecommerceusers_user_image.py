# Generated by Django 5.1.3 on 2024-12-07 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_ecommerceusers_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecommerceusers',
            name='user_image',
            field=models.FileField(upload_to='images/'),
        ),
    ]
