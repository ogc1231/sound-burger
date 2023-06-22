from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class PostAdmin(SummernoteModelAdmin):
    # list_display = ('title', 'slug', 'is_public', 'created')
    search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_public', 'created')
    summernote_fields = ('content')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(is_public=True)
