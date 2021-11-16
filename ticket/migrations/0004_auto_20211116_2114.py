# Generated by Django 3.2.8 on 2021-11-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20211116_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='amount',
            field=models.IntegerField(verbose_name='Количество билетов'),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Стоимость билета'),
        ),
        migrations.AlterField(
            model_name='party',
            name='constraint',
            field=models.IntegerField(verbose_name='Возрастное ограничение'),
        ),
    ]
