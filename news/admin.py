from django.contrib import admin
from .models import Category, News, Comments


admin.site.register(Category)

class AdminNews(admin.ModelAdmin):

    list_display = ('title','category','add_time')
    list_editable = ['category']
    list_display_links = ('title',)
    list_per_page = 20

admin.site.register(News, AdminNews)


class AdminComment(admin.ModelAdmin):
    list_display = ('news', 'email', 'comment')
    list_per_page = 20

admin.site.register(Comments, AdminComment)