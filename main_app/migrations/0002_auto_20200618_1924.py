# Generated by Django 3.0.7 on 2020-06-18 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='Test User', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='current_city',
            field=models.CharField(max_length=50),
        ),
    ]
