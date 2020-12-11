# Generated by Django 3.0.4 on 2020-04-16 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200416_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headlines',
            name='concern',
            field=models.CharField(choices=[('Headline', 'Headline'), ('Alert', 'Alert'), ('Notification', 'Notification'), ('Students', 'Students'), ('Teachers', 'Teachers')], default='Headline', help_text='For whom the Articles belongs to.', max_length=20),
        ),
        migrations.AlterField(
            model_name='headlines',
            name='description',
            field=models.TextField(help_text='Short Description favourable Max Lenght 250 Characters', max_length=500),
        ),
        migrations.AlterField(
            model_name='headlines',
            name='point1',
            field=models.CharField(blank=True, help_text='Short Points Considerable', max_length=150),
        ),
        migrations.AlterField(
            model_name='headlines',
            name='point2',
            field=models.CharField(blank=True, help_text='Short Points Considerable', max_length=150),
        ),
        migrations.AlterField(
            model_name='headlines',
            name='title',
            field=models.CharField(help_text='Title should be unique for a Day', max_length=100, unique_for_date='created'),
        ),
    ]
