from .views import login
from django.contrib.auth import views as auth_views
from django.urls import path, include
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page': '/'}, name='logout')
]
