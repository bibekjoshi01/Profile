# Generated by Django 4.1.3 on 2022-11-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('relationship', models.CharField(choices=[('Single', 'Single'), ('In a Relationship', 'In a Relationship'), ('Married', 'Married')], default='Single', max_length=20)),
                ('bio', models.CharField(max_length=150, null=True)),
                ('email', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
