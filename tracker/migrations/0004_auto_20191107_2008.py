# Generated by Django 2.2.7 on 2019-11-07 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20191107_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='supporter',
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='habit',
            name='supporters',
            field=models.ManyToManyField(blank=True, related_name='supporter', to='tracker.Supporter'),
        ),
    ]
