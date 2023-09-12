# Generated by Django 4.2.4 on 2023-09-08 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_author_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('date_of_start', models.DateField()),
                ('date_of_the_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('student_average_grade', models.IntegerField()),
                ('courses', models.ManyToManyField(blank=True, null=True, to='application.courses')),
            ],
        ),
    ]
