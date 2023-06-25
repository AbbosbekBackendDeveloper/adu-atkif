# Generated by Django 4.2.2 on 2023-06-25 22:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Kategoriya')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ism')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Sarlavha')),
                ('slug', models.SlugField(max_length=250)),
                ('body', models.TextField(verbose_name='Yangilik matni')),
                ('image', models.ImageField(upload_to='news/images', verbose_name='Rasm')),
                ('published_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Yuklagan vaqti')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Tahrirlangan vaqti')),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'published')], default='DF', max_length=2, verbose_name='Holati')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='news.category')),
            ],
            options={
                'ordering': ['-published_time'],
            },
        ),
    ]