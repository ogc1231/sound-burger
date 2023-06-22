from django.shortcuts import render
# from django.views import generic
from .models import Review


# class ReviewList(generic.ListView):
#     model = Review
#     queryset = Review.objects.filter(is_public=True).order_by('created')
#     template_name = 'index.html'
#     paginate_by = 12

def get_review_list(request):
    review_list = Review.objects.all
    queryset = Review.objects.filter(is_public=True).order_by('created')
    paginate_by = 12

    context = {
        'review_list': review_list,
    }
    return render(request, 'reviews/reviews.html', context)

# def get_menu_list(request):
#     food_list = Food.objects.all()

#     context = {
#         'food_list': food_list,
#     }
#     return render(request, 'menu/menu_list.html', context)

