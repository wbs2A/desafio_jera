from django.shortcuts import render
from django.utils.translation import get_language
from django.conf import settings
import requests


def homepage(request):
    url = 'https://api.themoviedb.org/3/movie/popular'
    query = {"api_key": settings.TMDB_API_KEY, "language": get_language(), 'sort_by': 'popularity.desc'}

    headers = {
        'cache-control': "no-cache",
    }
    context = {"data": requests.request("GET", url, headers=headers, params=query).text,
               "lang": get_language()
              }
    return render(request, template_name='moviesplatform/homepage.html', context=context)