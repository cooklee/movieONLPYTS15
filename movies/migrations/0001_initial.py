# Generated by Django 4.2.5 on 2023-09-27 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=123)),
                ('last_name', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='MoviePerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=123)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directed', to='movies.person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='screenplay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='written', to='movies.person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='starring',
            field=models.ManyToManyField(related_name='played', through='movies.MoviePerson', to='movies.person'),
        ),
    ]
