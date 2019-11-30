from django.urls import path
from .views import homepage, search, show_movie

urlpatterns = [
    path('', homepage, name='homepage'),
    path('busca/', search, name='search_movie'),
    path('filme/<int:movieid>', show_movie, name='movie_info'),

]
