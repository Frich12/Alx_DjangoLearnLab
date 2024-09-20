from django.shortcuts import render

def home(request):
    return render(request, 'blog/base.html')


from django.shortcuts import render
from django.views.generic import ListView
from .models import Post  

class PostListView(ListView):
    model = Post
    template_name = 'blog/base.html'  
    context_object_name = 'posts'

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'  

class RegisterView(TemplateView):
    template_name = 'blog/login.html'  



