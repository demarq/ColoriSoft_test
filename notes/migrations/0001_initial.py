# Generated by Django 2.1 on 2018-08-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Where is my Title? :(', max_length=50, verbose_name='Title')),
                ('text', models.CharField(default='Where is my Text? :(', max_length=300, verbose_name='Note')),
                ('unique_symbols', models.IntegerField(default=0, verbose_name='Unique symbols counter')),
            ],
        ),
    ]