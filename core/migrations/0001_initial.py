# Generated by Django 3.0.3 on 2020-03-06 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=150)),
                ('flag_image', models.ImageField(upload_to='flags/')),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='rights/')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='laws/')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Country')),
            ],
        ),
    ]
