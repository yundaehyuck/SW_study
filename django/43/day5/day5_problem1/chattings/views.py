from django.shortcuts import render,redirect
from .forms import ChatForm
from .models import Chat
from django.http import Http404
from django.views.decorators.http import require_http_methods, require_safe, require_POST


# Create your views here.

@require_safe
def index(request):

    chattings = Chat.objects.all()
    context = {
        'chattings':chattings,
    }

    return render(request,'chattings/index.html',context)

@require_http_methods(['GET','POST'])
def create(request):

    form = ChatForm(request.POST)
    if form.is_valid():
        chat = form.save()
        return redirect('chattings:detail',chat.pk)
    
    else:

        form = ChatForm()

    context = {
        'form':form
    }
    return render(request,'chattings/create.html',context)

@require_safe
def detail(request,pk):

    try:

        chat = Chat.objects.get(pk=pk)
        context = {
            'chat':chat,
        }
        return render(request,'chattings/detail.html',context)
    
    except Chat.DoesNotExist:
        raise Http404("No page")

@require_POST
def delete(request,pk):

    try:

        chat = Chat.objects.get(pk=pk)
        chat.delete()
        return redirect('chattings:index')
    
    except Chat.DoesNotExist:
        raise Http404("No id")

    
