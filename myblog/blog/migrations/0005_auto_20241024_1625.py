# Generated by Django 3.2 on 2024-10-24 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20241024_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category'),
            preserve_default=False,
        ),
    ]