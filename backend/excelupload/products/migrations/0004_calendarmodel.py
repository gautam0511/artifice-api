# Generated by Django 4.2 on 2023-07-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_state_productmodel_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendarmodel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('start_date', models.CharField(max_length=255)),
                ('end_date', models.CharField(max_length=255)),
            ],
        ),
    ]