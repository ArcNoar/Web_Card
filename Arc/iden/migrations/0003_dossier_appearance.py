# Generated by Django 4.1 on 2022-08-21 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iden', '0002_dossier_delete_user_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossier',
            name='appearance',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]