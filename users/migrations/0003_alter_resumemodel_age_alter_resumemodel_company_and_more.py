# Generated by Django 4.1.3 on 2022-12-07 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_resumemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumemodel',
            name='age',
            field=models.IntegerField(verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='resumemodel',
            name='company',
            field=models.CharField(max_length=50, verbose_name='предыдущее место работы'),
        ),
        migrations.AlterField(
            model_name='resumemodel',
            name='experience',
            field=models.IntegerField(verbose_name='стаж'),
        ),
        migrations.AlterField(
            model_name='resumemodel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='resumemodel',
            name='position',
            field=models.CharField(max_length=50, verbose_name='должность'),
        ),
        migrations.AlterField(
            model_name='resumemodel',
            name='surname',
            field=models.CharField(max_length=50, verbose_name='фамилия'),
        ),
    ]
