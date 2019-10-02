# Generated by Django 2.2.6 on 2019-10-02 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournaments', '0002_tournament_singleplayer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rozhodci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turnaj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]