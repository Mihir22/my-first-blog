# Generated by Django 2.2.5 on 2019-10-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=248)),
                ('l_name', models.CharField(max_length=248)),
                ('email', models.CharField(max_length=248)),
            ],
        ),
    ]