# Generated by Django 3.0.4 on 2020-03-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogIn_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
    ]
