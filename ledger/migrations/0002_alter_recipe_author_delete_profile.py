# Generated by Django 5.0.2 on 2024-03-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]