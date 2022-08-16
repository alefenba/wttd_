# Generated by Django 4.0.4 on 2022-08-15 23:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_alter_subscription_cpf_alter_subscription_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='id',
        ),
        migrations.AddField(
            model_name='subscription',
            name='hash_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
