# Generated by Django 5.0.6 on 2024-05-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_category_categorie_alter_setting_coordinate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageforadmin',
            name='name',
            field=models.CharField(blank=True, default='undefined', max_length=255),
        ),
    ]
