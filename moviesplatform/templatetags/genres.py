import requests, json
from django import template
from django.conf import settings
from django.utils import translation


register = template.Library()


def find_genre(genr):
    data = [{"id": 28, "name": "Ação"}, {"id": 12, "name": "Aventura"},{"id": 16, "name": "Animação"}, {"id": 35, "name": "Comédia"}, {"id": 80, "name": "Crime"}, {"id": 99, "name": "Documentário"}, {"id": 18, "name": "Drama"}, {"id": 10751,"name": "Família"}, {"id": 14,"name": "Fantasia"}, {"id": 36, "name": "História"}, {"id": 27, "name": "Terror"}, {"id": 10402, "name": "Música"}, {"id": 9648, "name": "Mistério"}, {"id": 10749, "name": "Romance"}, {"id": 878, "name": "Ficção científica"}, {"id": 10770, "name": "Cinema TV"}, {"id": 53, "name": "Thriller"}, {"id": 10752, "name": "Guerra"}, {"id": 37, "name": "Faroeste"}]
    for g in data:
        if g['id'] == int(genr):
            return g['name']


@register.filter(name='genre')
def genre(genre_list):
    result = [find_genre(genre) for genre in genre_list]
    return result
