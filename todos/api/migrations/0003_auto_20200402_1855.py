# Generated by Django 3.0.4 on 2020-04-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_todoitem_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
