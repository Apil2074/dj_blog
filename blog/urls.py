from django.conf import settings
from django.urls import path, include
from . import views  
from django.conf.urls.static import static
  
urlpatterns = [  
    path('', views.hello, name='blog'), 
    path('tinymce/', include('tinymce.urls')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)