from django.shortcuts import render
from .models import Review


def get_review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/reviews.html', context)
