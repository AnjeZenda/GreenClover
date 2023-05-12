# Generated by Django 4.2.1 on 2023-05-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_snippet_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.CharField(max_length=300)),
                ('is_free', models.BooleanField(default=False)),
                ('km', models.PositiveIntegerField()),
            ],
        ),
    ]
