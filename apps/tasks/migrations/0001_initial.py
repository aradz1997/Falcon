# Generated by Django 3.2.9 on 2021-11-14 10:31

from django.db import migrations, models
import django.db.models.deletion
import enumchoicefield.fields
import tasks.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                 primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('priority', enumchoicefield.fields.EnumChoiceField(
                    default=tasks.models.Priority.LOW, enum_class=tasks.models.Priority, max_length=1)),
                ('status', enumchoicefield.fields.EnumChoiceField(
                    default=tasks.models.Status.BACKLOG, enum_class=tasks.models.Status, max_length=1)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                 primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('task_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]