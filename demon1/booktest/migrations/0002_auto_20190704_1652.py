# Generated by Django 2.2.3 on 2019-07-04 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroinfo',
            name='camp',
            field=models.CharField(choices=[('good', '光明'), ('bad', '黑暗')], default='good', max_length=5),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='gender',
            field=models.CharField(choices=[('man', '男'), ('woman', '女')], max_length=5),
        ),
    ]
