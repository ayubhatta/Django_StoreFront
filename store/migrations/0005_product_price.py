# Generated by Django 4.2.6 on 2024-04-04 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20240403_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
            preserve_default=False,
        ),
    ]