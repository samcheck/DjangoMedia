from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Movie
# Create your views here.

def index(request):
    latest_movies_added = Movie.objects.order_by('-date_added')[:5]
    context = {'latest_movies_added': latest_movies_added}
    return render(request, 'movies/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
