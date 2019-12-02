from .views import signup, profiles
from django.contrib.auth import views as auth_views
from django.urls import path, include
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page': '/'}, name='logout'),
    path('registrar/', signup, name='register'),
    path('perfis/', profiles, name='profiles_and_conf'),
    #path('assistidos/'),
    #path('lista/'),

]
