# Generated by Django 3.1.4 on 2020-12-23 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(default=0, max_length=10, unique=True)),
                ('Aadhar_Number', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('Is_Active', models.BooleanField()),
                ('street', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=10, null=True)),
                ('state', models.CharField(max_length=10, null=True)),
                ('Postal_Code', models.IntegerField(null=True)),
                ('School_or_College_name', models.CharField(max_length=100)),
                ('Year_of_Passing', models.IntegerField()),
                ('percentage', models.FloatField()),
                ('Account_Number', models.IntegerField()),
                ('Bank_Name', models.CharField(max_length=100)),
                ('IFSC_Code', models.IntegerField(unique=True)),
                ('Full_Name', models.CharField(max_length=100)),
                ('Date_of_birth', models.DateField()),
                ('Blood_Group', models.CharField(max_length=100)),
                ('Contact_Number_1', models.IntegerField()),
                ('Contact_Number_2', models.IntegerField(blank=True, null=True)),
                ('Email_ID_1', models.EmailField(max_length=254)),
                ('Email_ID_2', models.EmailField(blank=True, max_length=254, null=True)),
                ('Company_Name', models.CharField(max_length=100)),
                ('Job_Role', models.CharField(max_length=100)),
                ('Work_Experience_in_Years', models.IntegerField()),
            ],
        ),
    ]
