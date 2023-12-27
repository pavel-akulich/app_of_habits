# Generated by Django 5.0 on 2023-12-21 22:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward', models.TextField(verbose_name='вознаграждение за выполнение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'вознаграждение',
                'verbose_name_plural': 'вознаграждения',
            },
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200, verbose_name='место выполнения привычки')),
                ('execution_time', models.TimeField(verbose_name='время выполнения привычки')),
                ('action', models.TextField(verbose_name='действие')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('frequency', models.PositiveIntegerField(default=1, verbose_name='периодичность в днях')),
                ('time_to_complete', models.PositiveIntegerField(verbose_name='время на выполнение')),
                ('is_published', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('award', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.award', verbose_name='вознаграждение')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_habits', to='habits.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
