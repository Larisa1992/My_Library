# Generated by Django 2.2.6 on 2020-08-22 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='birth_year',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.TextField(),
        ),
    ]
