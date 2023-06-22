from django.shortcuts import render, redirect
from .models import Review


def get_review_list(request):
    review_list = Review.objects.all
    queryset = Review.objects.filter(is_public=True).order_by('created')

    context = {
        'review_list': review_list,
    }
    return render(request, 'reviews/reviews.html', context)


def add_review(request):
    if request.method == 'POST':
        author = Review.author
        title = request.POST.get('title')
        content = request.POST.get('body')
        Review.objects.create(title=title, content=content)

        return redirect('get_review_list')
    return render(request, 'reviews/add_review.html',)
