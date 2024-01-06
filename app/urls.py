from django.urls import path
from . import views

urlpatterns = [
    # path('', include('app.urls')),
    path('',views.home.as_view(),name="home"),
]