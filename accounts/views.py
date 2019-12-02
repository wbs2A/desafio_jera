from .forms import SignUpForm
from .models import Profile, Account, User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def profiles(request):
    context = {}
    user = User.objects.filter(email=request.user.email).get()
    context['conta'] = Account.objects.get(user=user)
    try:
        context['perfis'] = Profile.objects.get(account__id=context['conta'].id)
    except:
        context['perfis'] = None
    return render(request, 'accounts/configuration.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})