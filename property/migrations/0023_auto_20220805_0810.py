# Generated by Django 2.2.24 on 2022-08-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0022_auto_20220805_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
    ]