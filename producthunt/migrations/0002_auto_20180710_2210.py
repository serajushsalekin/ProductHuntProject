# Generated by Django 2.1a1 on 2018-07-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producthunt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='votes_total',
            field=models.IntegerField(default=0),
        ),
    ]
