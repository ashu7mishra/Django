# Generated by Django 4.1 on 2024-09-26 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(default="Scaler@123", max_length=55),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
