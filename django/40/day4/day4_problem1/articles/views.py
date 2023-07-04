from django.shortcuts import render,redirect
from .models import Article

# Create your views here.

def index(request):

    articles = Article.objects.all()

    context = {
        'articles':articles,
    }


    return render(request,'index.html',context)

def new(request):

    return render(request,'new.html')

def create(request):

    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    #return render(request,'index.html')
    #return redirect('detail', article.pk)
    return redirect('index')

def detail(request,pk):

    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request,'detail.html',context)

def delete(request,pk):

    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('index')