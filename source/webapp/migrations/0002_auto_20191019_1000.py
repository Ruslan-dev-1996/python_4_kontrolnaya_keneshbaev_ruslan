# Generated by Django 2.2 on 2019-10-19 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='polls', to='webapp.Poll', verbose_name='опрос'),
        ),
    ]
