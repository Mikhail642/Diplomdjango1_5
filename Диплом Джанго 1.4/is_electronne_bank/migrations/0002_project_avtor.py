# Generated by Django 2.2.12 on 2020-06-08 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('is_electronne_bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='avtor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_avtor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
