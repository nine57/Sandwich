# Generated by Django 4.0.3 on 2022-04-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwiches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandwich',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sandwich',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]