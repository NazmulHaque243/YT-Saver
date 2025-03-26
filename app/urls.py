from django.urls import path
from .views import home, select_format, stream_video

urlpatterns = [
    path('', home, name='home'),
    path('select_format/', select_format, name='select_format'),
    path('stream/<path:url>/<str:format_id>/', stream_video, name='stream_video'),
]
