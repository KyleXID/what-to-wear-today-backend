# Generated by Django 2.2 on 2019-05-07 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_useroption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useroption',
            old_name='HATECOLD',
            new_name='hate_cold',
        ),
        migrations.RenameField(
            model_name='useroption',
            old_name='HATEHOT',
            new_name='hate_hot',
        ),
    ]
