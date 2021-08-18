# Generated by Django 3.2.4 on 2021-07-01 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follow',
            field=models.ManyToManyField(blank=True, to='user.User'),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to='user.user')),
                ('user_following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='user.user')),
            ],
            options={
                'db_table': 'follows',
            },
        ),
    ]