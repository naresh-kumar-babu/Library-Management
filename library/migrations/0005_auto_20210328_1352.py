# Generated by Django 3.1.7 on 2021-03-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20210328_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='fine_amount',
            field=models.CharField(default='0', max_length=5, null=True),
        ),
    ]