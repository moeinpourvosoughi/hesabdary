# Generated by Django 4.2 on 2023-04-24 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('price', models.FloatField()),
                ('number', models.IntegerField()),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('expire_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gozaresh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Anbardari.products')),
            ],
        ),
    ]
