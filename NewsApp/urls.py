from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls'))
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


admin.site.site_title = "News"
admin.site.site_header = 'My News'
admin.site.index_title = 'welcome to News App'