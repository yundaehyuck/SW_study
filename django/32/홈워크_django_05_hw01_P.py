def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            #유효성 검사를 통과한 데이터는 cleaned_data dict에 저장
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            article = Article(title=title,content=content)
            article.save() #만들어낸 article instance를 저장
            return redirect('articles:detail',article.pk)
    form = ArticleForm()
    context = {
        'form':form
    }
    return render(request,'articles/create.html',context)
