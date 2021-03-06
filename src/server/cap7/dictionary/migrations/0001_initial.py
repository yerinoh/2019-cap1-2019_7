# Generated by Django 2.2.1 on 2019-05-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.URLField(default='')),
                ('ref_word', models.TextField(null=True)),
                ('mean', models.TextField(null=True)),
                ('part', models.CharField(default='', max_length=10)),
                ('word', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Finger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.URLField(default='')),
                ('ref_word', models.TextField(null=True)),
                ('mean', models.TextField(null=True)),
                ('part', models.CharField(default='', max_length=10)),
                ('word', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.URLField(default='')),
                ('ref_word', models.TextField(null=True)),
                ('mean', models.TextField(null=True)),
                ('part', models.CharField(default='', max_length=10)),
                ('word', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
