from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200,)
    category_image = models.ImageField(upload_to='images/')

    class Meta:
        #  renaming ..
        verbose_name_plural='Category'


    def __str__(self):
        return self.title


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to='images/', blank=True)
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)


    class Meta:
       verbose_name_plural = 'News'

    def __str__(self):
        return self.title

class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name =  models.CharField(max_length=200)
    email =  models.EmailField(max_length=200)
    comment = models.TextField()
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.comment