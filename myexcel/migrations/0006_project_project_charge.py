# Generated by Django 2.2.4 on 2019-09-22 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myexcel', '0005_auto_20190916_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_charge',
            field=models.CharField(default='赵旻', max_length=50, verbose_name='项目负责人'),
        ),
    ]
