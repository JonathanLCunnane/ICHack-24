# Generated by Django 5.0.1 on 2024-02-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('A', 'A level'), ('G', 'GCSE'), ('K', 'KS3')], default='A', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.CharField(default='asdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='asdf', max_length=100),
            preserve_default=False,
        ),
    ]