# Generated by Django 5.1 on 2024-10-28 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0003_haber_resim'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='haber',
            name='resim',
        ),
        migrations.CreateModel(
            name='Resim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='haber_resimleri/')),
                ('haber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resimler', to='haber.haber')),
            ],
        ),
    ]
