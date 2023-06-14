from django.shortcuts import render
from .models import Review
from .forms import ReviewForm


def get_review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
        'review_form': ReviewForm()
    }
    return render(request, 'reviews/reviews.html', context)
