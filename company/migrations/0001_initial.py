# Generated by Django 3.1.4 on 2020-12-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('company_city', models.CharField(max_length=255, verbose_name='Company Name')),
                ('company_address', models.CharField(max_length=255, verbose_name='Company Address')),
                ('company_contact', models.IntegerField(default=0, verbose_name='Company Contact')),
                ('company_manager', models.CharField(max_length=255, verbose_name='Company Manager')),
                ('creater', models.CharField(max_length=255, verbose_name='Who Created')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'data id',
                'verbose_name_plural': 'data id',
                'db_table': 'company',
                'ordering': ['company_name'],
            },
        ),
    ]
