# Generated by Django 4.1.5 on 2023-02-26 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='Ticket_class',
            new_name='ticket_class',
        ),
    ]
