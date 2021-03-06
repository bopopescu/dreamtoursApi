# Generated by Django 3.0.6 on 2020-05-25 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dreamtours_app', '0009_auto_20200525_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamtours_app.Local'),
        ),
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamtours_app.User'),
        ),
        migrations.AlterField(
            model_name='local',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamtours_app.City'),
        ),
        migrations.AlterField(
            model_name='local',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamtours_app.Company'),
        ),
        migrations.AlterField(
            model_name='local',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamtours_app.LocalType'),
        ),
        migrations.AlterField(
            model_name='particular',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamtours_app.City'),
        ),
        migrations.AlterField(
            model_name='particular',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamtours_app.User'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamtours_app.Local'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='particular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamtours_app.Particular'),
        ),
    ]
