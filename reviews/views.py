from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


def get_review_list(request):
    review_list = Review.objects.all
    # queryset = Review.objects.filter(is_public=True).order_by('created')

    context = {
        'review_list': review_list,
    }
    return render(request, 'reviews/reviews.html', context)


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        # author = Review.author
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # Review.objects.create(title=title, content=content)
            return redirect('get_review_list')
    form = ReviewForm
    context = {
        'form': form
    }
    return render(request, 'reviews/add_review.html', context)
