# Generated by Django 4.1.1 on 2022-09-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiwi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
