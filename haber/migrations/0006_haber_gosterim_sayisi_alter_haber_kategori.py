# Generated by Django 5.1 on 2024-10-30 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0005_haber_resim_alter_haber_kategori_delete_resim'),
    ]

    operations = [
        migrations.AddField(
            model_name='haber',
            name='gosterim_sayisi',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='haber',
            name='kategori',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='haberler', to='haber.kategori'),
            preserve_default=False,
        ),
    ]
