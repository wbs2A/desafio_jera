import json

import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import translation

from .forms import SignUpForm, ProfileForm
from django.views.generic import CreateView
from .models import Profile, Account, User, Movie
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def profiles(request):
    context = {}
    user = User.objects.filter(email=request.user.email).get()
    context['conta'] = Account.objects.get(user=user)
    try:
        context['perfis'] = Profile.objects.filter(account__id=context['conta'].id).all()
    except:
        context['perfis'] = None
    return render(request, 'accounts/configuration.html', context)


@login_required
def set_profile(request, account, profile):
    user = User.objects.filter(email=request.user.email).get()
    acc = Account.objects.get(user=user)
    print(profile)
    acc.__setattr__('current_profile ', profile)
    acc.current_profile = profile
    acc.save()
    return redirect('/accounts/perfis/')

@login_required
def add_movie(request,movie_id):
    url = 'https://api.themoviedb.org/3/movie/'+str(movie_id)
    query = {"api_key": settings.TMDB_API_KEY, "language": translation.get_language()}
    response = requests.request("GET", url, params=query)
    response_data = json.loads(response.text)
    _movie = Movie(movieid= response_data['id'], name=response_data['original_title'])
    _movie.save()
    user = User.objects.filter(email=request.user.email).get()
    acc = Account.objects.get(user=user)
    prof = Profile.objects.get(pk=acc.current_profile)
    prof.movies_list.add(_movie)
    prof.save()
    return redirect('/')


@login_required
def my_list(request):
    user = User.objects.filter(email=request.user.email).get()
    acc = Account.objects.get(user=user)
    prof = Profile.objects.get(pk=acc.current_profile)
    context = {'movies': prof.movies_list.all()}
    return render(request, 'accounts/my_list.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.account.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})


class CreateProfile(CreateView):
    model = Profile
    fields = ['name', 'image', 'account']
    success_url = reverse_lazy('profiles_and_conf')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)