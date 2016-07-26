# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0002_review_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='interest',
            field=models.PositiveIntegerField(blank=True, help_text='Puntuación del 1 al 10', null=True, verbose_name='Interés General'),
        ),
        migrations.AlterField(
            model_name='review',
            name='newness',
            field=models.PositiveIntegerField(blank=True, help_text='Puntuación del 1 al 10', null=True, verbose_name='Novedad'),
        ),
        migrations.AlterField(
            model_name='review',
            name='relevance',
            field=models.PositiveIntegerField(blank=True, help_text='Puntuación del 1 al 10', null=True, verbose_name='Relevancia'),
        ),
    ]