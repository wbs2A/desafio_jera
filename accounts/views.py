from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Profile, Account, User
from .forms import SignUpForm, ProfileForm
from django.views.generic import CreateView
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