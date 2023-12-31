# Generated by Django 4.2.3 on 2023-09-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EndpointData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_name', models.CharField(default='my_name', max_length=255)),
                ('track', models.CharField(default='backend', max_length=255)),
                ('github_file_url', models.URLField(default='https://github.com/millenium2023')),
                ('github_repo_url', models.URLField(default='https://github.com/millenium2023')),
            ],
        ),
    ]
