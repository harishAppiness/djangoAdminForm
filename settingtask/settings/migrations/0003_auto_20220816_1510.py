# Generated by Django 3.1.7 on 2022-08-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_applicationsettings_module_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationsettings',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='applicationsettings',
            name='setting_value',
            field=models.CharField(max_length=250),
        ),
    ]
