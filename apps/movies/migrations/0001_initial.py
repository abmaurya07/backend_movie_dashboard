# Generated by Django 5.1.5 on 2025-01-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('one_line', models.TextField()),
                ('stars', models.TextField()),
                ('votes', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('gross', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['year'], name='movies_movi_year_82d175_idx'), models.Index(fields=['rating'], name='movies_movi_rating_8fd49a_idx'), models.Index(fields=['votes'], name='movies_movi_votes_6b174f_idx'), models.Index(fields=['gross'], name='movies_movi_gross_ad07d3_idx')],
            },
        ),
    ]
