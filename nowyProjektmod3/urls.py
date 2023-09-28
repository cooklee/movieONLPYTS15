"""
URL configuration for nowyProjektmod3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies import views
from cookieeees import views as cookie_views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.IndexView.as_view()),
    path('add_person/', views.AddPersonView.as_view()),
    path('persons/', views.ListPersonsView.as_view()),
    path('edit_person/<int:id>/', views.EditPersonView.as_view()),
    path('delete_person/<int:id>/', views.DeletePersonView.as_view()),
    path('add_genre/', views.AddGenreView.as_view()),
    path('genres/', views.ListGenresView.as_view()),
    path('edit_genre/<int:id>/', views.EditGenreView.as_view()),
    path('delete_genre/<int:id>/', views.DeleteGenreView.as_view()),
    path('add_movie/', views.AddMovieView.as_view()),
    path('movies/', views.ListMovieView.as_view()),
    path('edit_movie/<int:id>/', views.EditMovieView.as_view()),
    path('add_actor_to_movie/<int:movie_id>/', views.AddActorToMovieView.as_view()),
    path('cookie/', cookie_views.SetCookiesView.as_view())
]
