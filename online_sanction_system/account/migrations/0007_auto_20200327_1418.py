# Generated by Django 3.0.3 on 2020-03-27 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0006_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pic')),
                ('full_name', models.CharField(blank=True, max_length=50)),
                ('sid', models.CharField(blank=True, max_length=50)),
                ('branch', models.CharField(blank=True, max_length=50)),
                ('year', models.CharField(blank=True, max_length=1)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('DOB', models.DateField(blank=True)),
                ('mobile_number', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
    ]
