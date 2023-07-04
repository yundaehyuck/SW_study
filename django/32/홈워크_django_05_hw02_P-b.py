def create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('reservation:detail',article.pk)
    else:
        form = ReservationForm()
    #POST로 받지만, 유효성 검사를 통과하지 못하는 경우에도
    #작성페이지로 렌더링해줘야함
    context={
        'form':form
    }
    return render(request,'reservation/create.html',context)
