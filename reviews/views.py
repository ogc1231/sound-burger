from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from django.contrib import messages
from .forms import ReviewForm


def get_review_list(request):
    review_list = Review.objects.all

    context = {
        'review_list': review_list,
    }
    return render(request, 'reviews/reviews.html', context)


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Review added')

    form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'reviews/add_review.html', context)


def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review edited')
            return redirect('get_review_list')
    form = ReviewForm(instance=review)
    context = {
        'form': form
    }
    return render(request, 'reviews/edit_review.html', context)


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    messages.error(request, 'Review deleted')
    return redirect('get_review_list')
