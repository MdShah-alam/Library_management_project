# Generated by Django 4.2.4 on 2023-10-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Mystery', 'Mystery'), ('Thriller', 'Thriller'), ('Sci_Fi', 'Sci_Fi'), ('Humor', 'Humor'), ('Horror', 'Horror')], max_length=10)),
                ('count', models.IntegerField()),
                ('avialable', models.BooleanField()),
                ('first_pub', models.DateTimeField(auto_now_add=True)),
                ('last_pub', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BookStoreModel',
        ),
    ]
