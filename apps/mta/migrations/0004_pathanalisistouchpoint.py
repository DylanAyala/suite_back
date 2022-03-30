# Generated by Django 4.0.3 on 2022-03-30 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_campaign'),
        ('mta', '0003_pathsmetrics_mtaresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='PathAnalisisTouchpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(help_text='Date')),
                ('touchpoints_quantity', models.FloatField(blank=True, default=0, help_text='total_paths')),
                ('paths_count', models.FloatField(blank=True, default=0, help_text='total_paths')),
                ('advertiser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MTAPathAnalisisTouchpoint_Advertiser', to='system.advertiser')),
                ('campaign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MTAPathAnalisisTouchpoint_Campaign', to='system.campaign')),
                ('conversion_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MtaPathAnalisisTouchpoint_conversionType', to='mta.conversiontype')),
            ],
            options={
                'verbose_name_plural': 'MTA Path Analisis Touchpoint',
            },
        ),
    ]
