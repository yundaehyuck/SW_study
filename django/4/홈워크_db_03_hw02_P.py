def detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    comment_form = CommentForm()

    count_a = question.comment_set.filter(pick=False).count()
    count_b = question.comment_set.filter(pick=True).count()
    total_count = count_a+count_b

    per_a = 0
    per_b = 0
    if total_count:
        per_a = round(count_a / total_count * 100, 1)
        per_b = round(count_b / total_count * 100, 1)

    comments = question.comment_set.order_by('created_at').reverse()
    context = {
        'question': question,
        'comment_form': comment_form,
        'count_a': count_a,
        'count_b': count_b,
        'per_a': per_a,
        'per_b': per_b,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)
