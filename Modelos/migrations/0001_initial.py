# Generated by Django 4.1 on 2023-03-10 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=40)),
                ('fecha_registro', models.DateField()),
            ],
        ),
    ]
