# Generated by Django 4.2.2 on 2023-06-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finconsult', '0002_profile_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='birth_date',
            new_name='meeting_date',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
