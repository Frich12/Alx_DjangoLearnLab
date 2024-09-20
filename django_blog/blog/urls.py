from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home')
]

from django.urls import path
from .views import PostListView, LoginView, RegisterView  # Adjust imports based on your view functions

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]

