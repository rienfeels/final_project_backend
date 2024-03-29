# Generated by Django 5.0.3 on 2024-03-11 18:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsc_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='stripingform',
            name='form_data',
        ),
        migrations.AddField(
            model_name='stripingform',
            name='road_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='stripingform',
            name='size_of_white_paint_line',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='stripingform',
            name='size_of_yellow_paint_line',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='stripingform',
            name='white_paint_footage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='stripingform',
            name='yellow_paint_footage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='stripingform',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fsc_app.project'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
