# Generated by Django 2.2.3 on 2019-07-04 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoteTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VoteAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=20)),
                ('num', models.CharField(max_length=10)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voteproject.VoteTitle')),
            ],
        ),
    ]
