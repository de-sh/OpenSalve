# Generated by Django 2.1.1 on 2018-09-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='id',
            field=models.AutoField(help_text='Unique ID of request', primary_key=True, serialize=False),
        ),
    ]
