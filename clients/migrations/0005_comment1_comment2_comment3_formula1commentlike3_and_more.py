# Generated by Django 4.1.3 on 2022-12-16 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Formula1', '0004_commentformula1video_formula1video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Formula1_comments1', to='Formula1.comment')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Comment2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Formula1_comments2', to='Formula1.comment1')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Comment3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Formula1_comments3', to='Formula1.comment2')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Formula1CommentLike3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Formula1.comment3')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Formula1CommentLike2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Formula1.comment2')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Formula1CommentLike1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Formula1.comment1')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment3',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='Formula1comment_user3', through='Formula1.Formula1CommentLike3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment3',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Formula1.comment3'),
        ),
        migrations.AddField(
            model_name='comment3',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Formula1comments3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment2',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='Formula1comment_user2', through='Formula1.Formula1CommentLike2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment2',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Formula1.comment2'),
        ),
        migrations.AddField(
            model_name='comment2',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Formula1comments2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment1',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='Formula1comment_user1', through='Formula1.Formula1CommentLike1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment1',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Formula1.comment1'),
        ),
        migrations.AddField(
            model_name='comment1',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Formula1comments1', to=settings.AUTH_USER_MODEL),
        ),
    ]