# Generated by Django 4.1 on 2024-01-26 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PyBlog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'py_blog',
            },
        ),
    ]
