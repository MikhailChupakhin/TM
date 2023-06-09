# Generated by Django 4.2.1 on 2023-05-24 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Задача')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Детали')),
                ('task_date', models.DateField(auto_now=True, verbose_name='Дата создания')),
                ('is_done', models.BooleanField(default=False, verbose_name='Выполнена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.category', verbose_name='Категория')),
            ],
        ),
    ]
