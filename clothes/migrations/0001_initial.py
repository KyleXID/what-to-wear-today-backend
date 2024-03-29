# Generated by Django 2.2.1 on 2019-05-06 06:00

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_user_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=200)),
                ('user_gender', models.CharField(choices=[(user.models.Gender('M'), 'M'), (user.models.Gender('F'), 'F')], max_length=3)),
                ('img_ref', models.CharField(max_length=200)),
                ('page_ref', models.CharField(max_length=200)),
                ('temp_min', models.CharField(max_length=20)),
                ('temp_max', models.CharField(max_length=20)),
                ('hearts', models.ManyToManyField(related_name='hearts', to='user.User')),
            ],
            options={
                'db_table': 'clothes',
            },
        ),
    ]
