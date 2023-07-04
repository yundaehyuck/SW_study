from django.shortcuts import render,redirect
from .forms import MoviesForm
from .models import Movies
from django.http import Http404
from django.views.decorators.http import require_http_methods, require_safe, require_POST

# Create your views here.

@require_safe
def index(request):

    movies = Movies.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html',context)

@require_http_methods(['GET','POST'])
def create(request):

    if request.method == "POST":

        form = MoviesForm(request.POST)

        if form.is_valid():

            movies = form.save()

            return redirect('movies:detail',movies.pk)
    
    else:

        form = MoviesForm()
    
    context = {
        'form':form
    }

    return render(request,'movies/create.html',context)

@require_safe
def detail(request,pk):

    try:

        movies = Movies.objects.get(pk=pk)

        context = {
            'movies':movies,
        }

        return render(request,'movies/detail.html',context)
    
    except Movies.DoesNotExist:

        raise Http404("No page")

@require_POST
def delete(request,pk):

    movies = Movies.objects.get(pk=pk)
    if request.method == "POST":
        movies.delete()
        return redirect("movies:index")

    return redirect('movies:detail',movies.pk)

@require_http_methods(['GET','POST'])
def update(request,pk):

    movies = Movies.objects.get(pk=pk)
    if request.method == "POST":
        form  = MoviesForm(request.POST, initial = request.POST, instance=movies)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movies.pk)
    
    else:
        form = MoviesForm(instance=movies)

    context = {
        'form':form,
        'movies':movies,
    }
    
    return render(request, 'movies/update.html',context)
