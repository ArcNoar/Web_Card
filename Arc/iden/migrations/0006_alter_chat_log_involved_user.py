# Generated by Django 4.1 on 2023-09-14 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iden', '0005_characters_chat_log_tg_users_character_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_log',
            name='involved_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iden.tg_users'),
        ),
    ]
