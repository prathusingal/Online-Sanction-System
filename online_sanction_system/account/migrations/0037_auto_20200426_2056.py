# Generated by Django 3.0.3 on 2020-04-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0036_auto_20200425_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditorium',
            name='progress',
            field=models.CharField(choices=[('None', '------'), ('in-progress', 'in-progress'), ('approved', 'approved'), ('dismissed', 'dismissed')], default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='auditorium',
            name='reason_for_disapproval',
            field=models.TextField(blank=True, default=None, help_text='Required, if you are going to disapprove the application', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='reason_for_disapproval',
            field=models.TextField(blank=True, default=None, help_text='Only required, if you are going to disapprove the application', null=True),
        ),
        migrations.AlterField(
            model_name='labs',
            name='place',
            field=models.CharField(choices=[('None', '------'), ('LAB-1(place-A)', 'LAB-1(place-A)'), ('LAB-1(place-B)', 'LAB-1(place-B)'), ('LAB-1(place-C)', 'LAB-1(place-C)'), ('LAB-1(place-D)', 'LAB-1(place-D)'), ('LAB-1(place-E)', 'LAB-1(place-E)'), ('LAB-2(place-A)', 'LAB-2(place-A)'), ('LAB-2(place-B)', 'LAB-2(place-B)'), ('LAB-2(place-C)', 'LAB-2(place-C)'), ('LAB-2(place-D)', 'LAB-2(place-D)'), ('LAB-2(place-E)', 'LAB-2(place-E)'), ('LAB-3(place-A)', 'LAB-3(place-A)'), ('LAB-3(place-B)', 'LAB-3(place-B)'), ('LAB-3(place-C)', 'LAB-3(place-C)'), ('LAB-3(place-D)', 'LAB-3(place-D)'), ('LAB-3(place-E)', 'LAB-3(place-E)'), ('LAB-4(place-A)', 'LAB-4(place-A)'), ('LAB-4(place-B)', 'LAB-4(place-B)'), ('LAB-4(place-C)', 'LAB-4(place-C)'), ('LAB-4(place-D)', 'LAB-4(place-D)'), ('LAB-4(place-E)', 'LAB-4(place-E)'), ('LAB-5(place-A)', 'LAB-5(place-A)'), ('LAB-5(place-B)', 'LAB-5(place-B)'), ('LAB-5(place-C)', 'LAB-5(place-C)'), ('LAB-5(place-D)', 'LAB-5(place-D)'), ('LAB-5(place-E)', 'LAB-5(place-E)')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='labs',
            name='progress',
            field=models.CharField(choices=[('None', '------'), ('in-progress', 'in-progress'), ('approved', 'approved'), ('dismissed', 'dismissed')], default='in-progress', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='labs',
            name='reason_for_disapproval',
            field=models.TextField(blank=True, default=None, help_text='Only required, if you are going to disapprove the application', null=True),
        ),
        migrations.AlterField(
            model_name='lecturehalls',
            name='progress',
            field=models.CharField(choices=[('None', '------'), ('in-progress', 'in-progress'), ('approved', 'approved'), ('dismissed', 'dismissed')], default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lecturehalls',
            name='reason_for_disapproval',
            field=models.TextField(blank=True, default=None, help_text='Only required, if you are going to disapprove the application', null=True),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='reason_for_disapproval',
            field=models.TextField(blank=True, default=None, help_text='Only required, if you are going to disapprove the application', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='DOB',
            field=models.DateField(blank=True, default=None, help_text='Use %YYYY-%MM-%DD format.', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_number',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sid',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year',
            field=models.CharField(choices=[('N', '------'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=None, max_length=1, null=True),
        ),
    ]