# Generated by Django 5.1.2 on 2024-10-26 16:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('script', '0002_script_total_dislikes_script_total_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'Like'), (-1, 'Dislike')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='script.script')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('script', 'user')},
            },
        ),
    ]