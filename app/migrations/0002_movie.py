# Generated by Django 2.0.6 on 2019-05-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieurl', models.CharField(max_length=150)),
                ('movieimg', models.CharField(max_length=150)),
                ('moviename', models.CharField(max_length=30)),
                ('actoranddirector', models.CharField(max_length=150)),
                ('grade', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('likemoviename', models.CharField(max_length=30)),
                ('unlikemoviename', models.CharField(max_length=30)),
            ],
        ),
    ]
