# Generated by Django 3.2.3 on 2021-07-07 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_usuario_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='passw',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
