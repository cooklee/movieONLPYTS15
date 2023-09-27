from django.shortcuts import render, redirect
from django.views import View

from movies.models import Person, Genre, Movie


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


# Create your views here.
class AddPersonView(View):

    def get(self, request):
        return render(request, 'form_person.html')

    def post(self, request):
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        p = Person.objects.create(first_name=imie, last_name=nazwisko)
        return redirect('/add_person/')


class ListPersonsView(View):
    def get(self, request):
        persons = Person.objects.all()
        return render(request, 'persons_list.html', {'persons': persons})

class EditPersonView(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        return render(request, 'form_person.html', {'person':person})

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        person.first_name = imie
        person.last_name = nazwisko
        person.save()
        return redirect('/persons/')


class DeletePersonView(View):


    def get(self,request, id):
        person = Person.objects.get(pk=id)
        return render(request, 'delete_form.html', {'object':person})

    def post(self, request, id):
        odp = request.POST['odp']
        if odp == 'Tak':
            Person.objects.get(pk=id).delete()
        return redirect('/persons/')

class DeleteGenreView(View):


    def get(self,request, id):
        genre = Genre.objects.get(pk=id)
        return render(request, 'delete_form.html', {'object':genre})

    def post(self, request, id):
        odp = request.POST['odp']
        if odp == 'Tak':
            Genre.objects.get(pk=id).delete()
        return redirect('/genres/')



class AddGenreView(View):

    def get(self, request):
        return render(request, 'form_genre.html')

    def post(self, request):
        name = request.POST['name']
        p = Genre.objects.create(name=name)
        return redirect('/add_genre/')


class ListGenresView(View):
    def get(self, request):
        genres = Genre.objects.all()
        return render(request, 'genre_list.html', {'genres': genres})

class EditGenreView(View):

    def get(self, request, id):
        genre = Genre.objects.get(pk=id)
        return render(request, 'form_genre.html', {'genre':genre})

    def post(self, request, id):
        genre = Genre.objects.get(pk=id)
        name = request.POST['name']

        genre.name = name
        return redirect('/genres/')



class AddMovieView(View):

    def get(self, request):
        persons = Person.objects.all()
        return render(request, 'form_movie.html', {'persons':persons})

    def post(self, request):
        title = request.POST.get('title')
        year = request.POST.get('year')
        rating = request.POST.get('rating')
        director_id = request.POST.get('director')
        # director = Person.objects.get(id=director_id)
        screenplay_id = request.POST.get('screenplay')
        # screenplay = Person.objects.get(id=screenplay_id)
        Movie.objects.create(title=title, year=year, rating=rating,
                             director_id=director_id, screenplay_id=screenplay_id)
        # Movie.objects.create(title=title, year=year, rating=rating,
        #                      director=director, screenplay=screenplay)

        return redirect('/add_movie/')


class ListMovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movie_list.html', {'movies': movies})

class EditMovieView(View):

    def get(self, request, id):
        movie = Movie.objects.get(pk=id)
        persons = Person.objects.all()
        return render(request, 'form_movie.html', {'movie':movie, 'persons':persons})

    def post(self, request, id):
        movie = Movie.objects.get(pk=id)
        title = request.POST.get('title')
        year = request.POST.get('year')
        rating = request.POST.get('rating')
        director_id = request.POST.get('director')
        screenplay_id = request.POST.get('screenplay')
        movie.title = title
        movie.year =year
        movie.rating = rating
        movie.screenplay_id = screenplay_id
        movie.director_id = director_id
        movie.save()
        return redirect('/genres/')



