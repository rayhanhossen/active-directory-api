# Generated by Django 3.2.4 on 2021-06-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('manager', models.CharField(blank=True, max_length=255, null=True)),
                ('SAM_account_name', models.CharField(blank=True, max_length=255)),
                ('pager', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('user_account_control', models.IntegerField(blank=True, default=546, null=True)),
                ('office', models.CharField(max_length=255)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('address3', models.CharField(max_length=255)),
                ('PO', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('division', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('parent_OU', models.CharField(max_length=255)),
                ('band', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=255)),
                ('status', models.IntegerField(blank=True, default=0, null=True)),
                ('joining_date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
