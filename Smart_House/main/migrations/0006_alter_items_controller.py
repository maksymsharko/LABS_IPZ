# Generated by Django 3.2.5 on 2021-10-28 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_items_controller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='controller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.controls'),
        ),
    ]
