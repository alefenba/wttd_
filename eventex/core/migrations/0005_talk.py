# Generated by Django 4.0.4 on 2022-08-11 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_contact_options_alter_contact_kind_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start', models.TimeField()),
                ('description', models.TextField()),
                ('speakers', models.ManyToManyField(to='core.speaker')),
            ],
        ),
    ]
