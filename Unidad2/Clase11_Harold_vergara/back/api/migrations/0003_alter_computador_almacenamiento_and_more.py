# Generated by Django 5.0.3 on 2024-04-05 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_computador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computador',
            name='almacenamiento',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='computador',
            name='marca',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='computador',
            name='memoriaRam',
            field=models.TextField(),
        ),
    ]
