# Generated by Django 3.1.3 on 2020-11-23 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('anons', models.CharField(max_length=250, verbose_name='Anons')),
                ('full_text', models.TextField(verbose_name='Article')),
                ('date', models.DateTimeField(verbose_name='PublishDate')),
            ],
        ),
    ]
