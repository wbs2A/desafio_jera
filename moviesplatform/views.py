from django.http import HttpResponse
from django.shortcuts import render
from django.utils import translation
from django.conf import settings
import requests, random
import json


def get_banner_movie(_id, headers, query):
    return requests.request("GET", 'https://api.themoviedb.org/3/movie/' + str(_id) + '/videos', headers=headers, params=query)


def get_popular_movies(urls, headers, query):
    json_data = {}
    for req in urls:
        response = requests.request("GET", req['url'], headers=headers, params=dict(query, **req['query']))
        json_data[req['name']] = json.loads(response.text)
    return json_data


def homepage(request):
    try:
        page = int(request.GET['page'])
    except:
        page = 1
    #conjunto de urls identificadas que serão utilizadas da API
    urls = [{'name': 'movies', 'url': 'https://api.themoviedb.org/3/movie/popular','query': {'sort_by': 'popularity.desc', "page": page}},{'name': 'genre', 'url': 'https://api.themoviedb.org/3/genre/movie/list', 'query': {}}]
    #Parâmetros de busca a serem passados para a API
    query = {"api_key": settings.TMDB_API_KEY, "language": translation.get_language()}

    #Cabeçalho da requisição
    headers = {    }

    json_data = get_popular_movies(urls, headers, query)

    context = {"movies": json_data['movies']['results'],
               'genres': json_data['genre']['genres'],
               'page': json_data['movies']['page'],
               'total_pages': json_data['movies']['total_pages'],
              }

    if page == 1:
        json_data['recomend'] = json.loads(get_banner_movie(json_data['movies']['results'][0]['id'], headers, query).text)
        print('entrei1')
        context['recomendation'] = json_data['recomend']['results'][0]['key']

    return render(request, template_name='moviesplatform/homepage.html', context=context)
