# Generated by Django 4.2.1 on 2023-06-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]