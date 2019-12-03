import json
import requests
from django.conf import settings
from urllib.parse import urlencode
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import translation


def get_banner_movie(_id, headers, query):
    return requests.request("GET", 'https://api.themoviedb.org/3/movie/' + str(_id) + '/videos', headers=headers, params=query)


def find_genre(genlist,genr):
    for g in genlist:
        if g['id'] == genre:
            return g['name']


def genre(genre_list):
    query = {"api_key": settings.TMDB_API_KEY, "language": translation.get_language()}
    headers = {}
    req = requests.request("GET", 'https://api.themoviedb.org/3/genre/movie/list', headers=headers, params=query)
    data = json.loads(req.text)['genres']
    result = [find_genre(data, genre) for genre in genre_list]
    return result


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
    urls = [{'name': 'movies', 'url': 'https://api.themoviedb.org/3/movie/popular','query': {'sort_by': 'popularity.desc', "page": page}}]
    #Parâmetros de busca a serem passados para a API
    query = {"api_key": settings.TMDB_API_KEY, "language": translation.get_language()}

    #Cabeçalho da requisição
    headers = {}

    json_data = get_popular_movies(urls, headers, query)

    context = {"movies": json_data['movies']['results'],
               'page': json_data['movies']['page'],
               'total_pages': json_data['movies']['total_pages'],
              }

    if page == 1:
        json_data['recomend'] = json.loads(get_banner_movie(json_data['movies']['results'][0]['id'], headers, query).text)
        context['recomendation'] = json_data['recomend']['results'][0]['key']

    return render(request, template_name='moviesplatform/homepage.html', context=context)


def search(request):
    try:
        page = int(request.GET['page'])
    except:
        page = 1
    url = 'https://api.themoviedb.org/3/search/movie'
    query = {"api_key": settings.TMDB_API_KEY, "language": translation.get_language(), 'query': request.POST.get('search_query'), "page": page}
    response = requests.request("GET", url, params=query)
    json_data = json.loads(response.text)
    context = {'result': json_data['results'],'page': json_data['page'], 'total_pages': json_data['total_pages']}
    return render(request, template_name='moviesplatform/results.html', context=context)


def show_movie(request, movieid):
    url = 'https://api.themoviedb.org/3/movie/'+str(movieid)
    query = {"api_key": settings.TMDB_API_KEY, "language": translation.get_language()}
    response = requests.request("GET", url, params=query)
    context = {'movie': json.loads(response.text)}
    return render(request, template_name='moviesplatform/movieinfo.html', context=context)