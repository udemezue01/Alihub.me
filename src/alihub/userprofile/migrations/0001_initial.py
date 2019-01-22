# Generated by Django 2.0.8 on 2019-01-22 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300, unique=True)),
                ('account_type', models.CharField(max_length=3000)),
                ('avatar', models.FileField(blank=True, upload_to='')),
                ('bio', models.CharField(blank=True, max_length=400, verbose_name='About')),
                ('website', models.CharField(blank=True, max_length=5000)),
                ('phone', models.IntegerField()),
                ('category', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accounts.User')),
            ],
        ),
    ]
