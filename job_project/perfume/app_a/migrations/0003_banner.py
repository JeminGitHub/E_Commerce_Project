# Generated by Django 4.2 on 2023-07-04 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_a', '0002_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bnr_btm_one', models.ImageField(upload_to='banner')),
                ('bnr_btm_two', models.ImageField(upload_to='banner')),
            ],
        ),
    ]
