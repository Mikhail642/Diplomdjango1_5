# Generated by Django 2.2.12 on 2020-06-12 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('is_electronne_bank', '0003_auto_20200608_1754'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Организации-партнеры', 'verbose_name_plural': 'Организации-партнеры'},
        ),
        migrations.AlterField(
            model_name='project',
            name='avtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_avtor', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
