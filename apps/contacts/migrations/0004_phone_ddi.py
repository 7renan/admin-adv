# Generated by Django 3.0.5 on 2020-04-30 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_remove_phone_ddi'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='ddi',
            field=models.CharField(default=55, max_length=2, verbose_name='DDI'),
            preserve_default=False,
        ),
    ]