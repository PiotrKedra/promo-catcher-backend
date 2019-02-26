# Generated by Django 2.1.7 on 2019-02-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190226_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='data_end',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='data_start',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='promotion_message',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='facebook_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_url',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]