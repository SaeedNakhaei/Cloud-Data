# Generated by Django 5.0.7 on 2024-07-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_object_uploadfile_alter_object_sharedlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='iformat',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Format'),
        ),
        migrations.AlterField(
            model_name='object',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Size'),
        ),
    ]
