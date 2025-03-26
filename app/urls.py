from django.urls import path
from .views import home, get_video_formats

urlpatterns = [
    path('', home, name='home'),
    path('get_formats/', get_video_formats, name='get_formats'),
]
