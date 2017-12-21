from django.conf.urls import url,include
from student import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^index/$', views.IndexView, name='index'),
    url(r'^index/(?P<id>[0-9]+)$', views.Cat, name='category'),
    url(r'^index/add/$', views.AddBook.as_view(), name='add-book')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#To access the MEDIA_URL in template you must add django.template.context_processors.media to your context_processeors inside the TEMPLATES config.