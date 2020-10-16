from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('index', views.MovieIndexView.as_view(), name='movie_view'),
    path('registration', views.MovieRegistrationView.as_view(), name='movie_registration')
]