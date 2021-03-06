# Generated by Django 3.2 on 2021-05-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=15)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('cardname', models.CharField(max_length=50)),
                ('cardnumber', models.IntegerField()),
            ],
        ),
    ]
