# Generated by Django 3.2.5 on 2021-10-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=100)),
                ('esal', models.IntegerField()),
                ('eaddr', models.CharField(max_length=100)),
            ],
        ),
    ]
