from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=123)
    year = models.IntegerField()
    rating = models.FloatField()
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='written')
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='directed')
    starring = models.ManyToManyField(Person, through='MoviePerson', related_name='played')
    genres = models.ManyToManyField(Genre)


    def __str__(self):
        return f"{self.title} {self.year} {self.rating}"


class MoviePerson(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=123)
