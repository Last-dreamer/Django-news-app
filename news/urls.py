from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('all', views.allNews, name="all"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('category', views.category, name="category"),
    path('category/<int:id>', views.category_news, name='category')
]