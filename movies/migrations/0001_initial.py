# Generated by Django 2.1.8 on 2019-05-16 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_path', models.TextField(blank=True)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_casts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_path', models.TextField(blank=True)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_directors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_genres', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField()),
                ('original_language', models.CharField(max_length=20)),
                ('original_title', models.TextField()),
                ('overview', models.TextField(blank=True)),
                ('release_date', models.CharField(max_length=30)),
                ('revenue', models.IntegerField()),
                ('runtime', models.IntegerField(blank=True)),
                ('tagline', models.TextField(blank=True)),
                ('title', models.TextField()),
                ('vote_average', models.FloatField()),
                ('role_data', models.TextField()),
                ('poster_path', models.TextField()),
                ('casts', models.ManyToManyField(related_name='movies', to='movies.Cast')),
                ('director', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='movies.Director')),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Review'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
