# Generated by Django 4.1.1 on 2022-11-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiwi', '0006_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=100)),
            ],
        ),
    ]