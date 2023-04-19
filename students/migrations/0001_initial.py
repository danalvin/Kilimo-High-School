# Generated by Django 4.1.5 on 2023-04-19 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('grade_level', models.IntegerField()),
                ('enrollment_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
