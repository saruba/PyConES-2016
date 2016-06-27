# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0012_auto_20160619_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='duration',
            field=models.PositiveIntegerField(blank=True, choices=[(15, '15 minutos'), (30, '30 minutos')], default=30, null=True, verbose_name='Duración'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='language',
            field=models.CharField(choices=[('es', 'Español'), ('en', 'Inglés')], default='es', max_length=2, verbose_name='Idioma'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='_abstract_ca_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='_abstract_en_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='_abstract_es_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='_abstract_eu_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='_abstract_gl_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='_additional_notes_ca_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='_additional_notes_en_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='_additional_notes_es_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='_additional_notes_eu_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='_additional_notes_gl_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract',
            field=markupfield.fields.MarkupField(blank=True, default='', help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", rendered_field=True, verbose_name='Resumen detallado'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_ca',
            field=markupfield.fields.MarkupField(blank=True, default='', help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", null=True, rendered_field=True, verbose_name='Resumen detallado'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_ca_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_en',
            field=markupfield.fields.MarkupField(blank=True, default='', help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", null=True, rendered_field=True, verbose_name='Resumen detallado'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_en_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_es',
            field=markupfield.fields.MarkupField(blank=True, default='', help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", null=True, rendered_field=True, verbose_name='Resumen detallado'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_es_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_eu',
            field=markupfield.fields.MarkupField(blank=True, default='', help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", null=True, rendered_field=True, verbose_name='Resumen detallado'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_eu_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_gl',
            field=markupfield.fields.MarkupField(blank=True, default='', help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", null=True, rendered_field=True, verbose_name='Resumen detallado'),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='abstract_gl_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_ca_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_en_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_es_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_eu_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_gl_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='proposalbase',
            name='additional_notes_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
    ]
