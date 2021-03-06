from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup, profiles, CreateProfile, set_profile, add_movie, my_list
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page': '/'}, name='logout'),
    path('registrar/', signup, name='register'),
    path('perfis/', profiles, name='profiles_and_conf'),
    path('novoperfil/', CreateProfile.as_view(), name='new_profile'),
    path('set_profile/<int:account>/<int:profile>', set_profile),
    path('add/<int:movie_id>/', add_movie),
    path('minhalista/', my_list, name='watch_list')
    #path('assistidos/'),
    #path('lista/'),

]
