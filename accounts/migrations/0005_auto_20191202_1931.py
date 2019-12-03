# Generated by Django 2.2.7 on 2019-12-02 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191202_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='movies_list',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.Movie'),
        ),
    ]