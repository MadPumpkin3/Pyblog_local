# Generated by Django 4.1 on 2024-01-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_pyblog_regist_dt_pyblog_update_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyblog',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
