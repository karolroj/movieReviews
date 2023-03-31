from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import movies as Movies

# Create your views here.
def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movies.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movies.objects.all()
    return render(
        request,
        'home.html',
        {'searchTerm': searchTerm, 'movies': movies}
    )

def about(request):
    return HttpResponse('<h1>About information</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})

def details(request, movie_id):
    movie = get_object_or_404(Movies,pk=movie_id)
    return render(request, 'details.html', {'movie': movie})
