# Generated by Django 4.2.6 on 2024-01-01 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_alter_bookmodel_category_commentmodel'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasemodel',
            name='book',
        ),
        migrations.RemoveField(
            model_name='purchasemodel',
            name='returned',
        ),
        migrations.AddField(
            model_name='purchasemodel',
            name='isBorrowed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchasemodel',
            name='Book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.bookmodel'),
        ),
    ]
