# Generated by Django 2.2.12 on 2020-06-07 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('is_electronne_bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnervproject',
            name='function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='function_partner', to='is_electronne_bank.Function', verbose_name='Функции'),
        ),
    ]