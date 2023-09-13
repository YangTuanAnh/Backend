# Generated by Django 4.2.5 on 2023-09-13 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0011_alter_customuser_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile",
            field=models.ForeignKey(
                default=1694605398.936703,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
    ]
