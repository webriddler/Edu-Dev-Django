# Generated by Django 3.0.4 on 2020-04-16 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200416_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headlines',
            name='concern',
            field=models.CharField(choices=[('Students', 'Students'), ('Teachers', 'Teachers'), ('Notification', 'Notification'), ('Alert', 'Alert'), ('Headline', 'Headline')], default='Headline', help_text='For whom the Articles belongs to.', max_length=20),
        ),
        migrations.AlterField(
            model_name='headlines',
            name='description',
            field=models.TextField(blank=True, help_text='Short Description favourable Max Lenght 250 Characters', max_length=500),
        ),
    ]