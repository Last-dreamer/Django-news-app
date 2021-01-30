from django.contrib import messages
from django.shortcuts import render
from .models import News, Category, Comments


def home(request):
    first_news = News.objects.all().order_by('-id').first()
    # first_news = News.objects.first()

    three_news = News.objects.all().order_by("-add_time")[1:4]

    category = Category.objects.all().order_by('-id')[0:5]

    context = {
        'first_news': first_news,
        'three_news': three_news,
        'categories': category,
    }
    return render(request, 'home.html', context)

def allNews(request):
    news = News.objects.all().order_by("-id")
    context = {
        'all_news': news,
    }
    return render(request, 'all_news.html', context)


def detail(request, id):

    detail = News.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['message']

        Comments.objects.create(
           news= detail,
            name=name,
           email=email,
           comment=comment
        )
        messages.success(request, 'comment successfully submitted...')

    category = Category.objects.get(id=detail.category.id)
    related_news = News.objects.filter(category=category).exclude(id=id).order_by("-add_time")
    comments = Comments.objects.filter(news=detail, status=True).order_by('-id')
    context = {
      'detail': detail,
      'related_news': related_news,
       'comments': comments
    }
    return render(request, 'detail.html', context)


def category(request):
    category = Category.objects.all().order_by("-id")
    context = {
     'category': category
    }
    return render(request, 'category.html', context)


def category_news(request, id):
    category = Category.objects.get(id=id)
    all_news = News.objects.filter(category=category).order_by("-add_time")

    context = {
        'category': category,
        'all_news': all_news,
    }
    return render(request, 'category_news.html', context)