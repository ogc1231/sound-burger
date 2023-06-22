from django.shortcuts import render

from .models import Review


def get_review_list(request):
    review_list = Review.objects.all
    queryset = Review.objects.filter(is_public=True).order_by('created')

    context = {
        'review_list': review_list,
    }
    return render(request, 'reviews/reviews.html', context)
