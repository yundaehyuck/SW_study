from django.shortcuts import render,redirect
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()

    context = {
        'movies':movies,
    }

    return render(request,'index.html',context)

def detail(request, pk):

    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
    }
    return render(request,'detail.html',context)

def delete(request, pk):

    movie = Movie.objects.get(pk=pk)
    movie.delete()

    return redirect('index')

def new(request):

    return render(request, 'new.html')

def create(request):

    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movie = Movie(title=title, audience=audience, release_date=release_date, genre=genre, score=score, poster_url=poster_url, description=description)
    movie.save()

    return redirect('index')

def edit(request,pk):

    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
        'genres':["코미디","액션","로맨스","범죄","SF","스포츠","판타지","전쟁","공포","스릴러","멜로","모험","미스터리","재난","애니메이션"]
    }

    return render(request,'edit.html',context)

def update(request,pk):

    movie = Movie.objects.get(pk=pk)

    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')

    movie.save()

    return redirect('detail',movie.pk)
    

