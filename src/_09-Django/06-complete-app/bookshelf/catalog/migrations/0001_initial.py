"""Pierwsza migracja – tworzenie tabel Author i Book."""
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Imię')),
                ('last_name',  models.CharField(max_length=100, verbose_name='Nazwisko')),
                ('birth_year', models.IntegerField(blank=True, null=True,
                                                   verbose_name='Rok urodzenia')),
                ('bio',        models.TextField(blank=True, verbose_name='Biogram')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autorzy',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('title',       models.CharField(max_length=200, verbose_name='Tytuł')),
                ('author',      models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='books',
                    to='catalog.author',
                    verbose_name='Autor',
                )),
                ('year',        models.IntegerField(blank=True, null=True,
                                                    verbose_name='Rok wydania')),
                ('isbn',        models.CharField(blank=True, max_length=20,
                                                 verbose_name='ISBN')),
                ('description', models.TextField(blank=True, verbose_name='Opis')),
                ('created_at',  models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Książka',
                'verbose_name_plural': 'Książki',
                'ordering': ['title'],
            },
        ),
    ]

