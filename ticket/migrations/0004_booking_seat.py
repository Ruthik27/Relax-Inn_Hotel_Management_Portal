# Generated by Django 3.2.6 on 2021-12-03 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0018_alter_seat_unique_together'),
        ('ticket', '0003_auto_20211118_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='seat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.seat'),
        ),
    ]
