# Generated by Django 2.1.7 on 2019-04-16 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0004_auto_20190416_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='external_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
