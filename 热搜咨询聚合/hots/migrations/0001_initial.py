# Generated by Django 5.0 on 2024-04-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='热点标题')),
                ('detail_url', models.CharField(max_length=255, verbose_name='详情页URL')),
            ],
        ),
    ]
