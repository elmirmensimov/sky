# Generated by Django 5.1 on 2024-11-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0006_haber_gosterim_sayisi_alter_haber_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='haber',
            name='on_bilgi',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]