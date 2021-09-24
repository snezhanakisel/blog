from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from .models import Article
from .forms import ArticleForm
from .forms import RegisterForm



def e_handler404(request, exception):
    return render(request, 'main/404.html')

def error404(request):
    return render(request, 'main/404.html')

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def blog(request):
    article = Article.objects.all()
    data = {
        'articles': article
    }
    return render(request, 'main/blog.html', data)




def show_article(request, post_slug):
    post = get_object_or_404(Article, slug=post_slug)
    data1 = {
        'post':post
    }
    return render(request, 'main/blog-single.html', data1)


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

        form = ArticleForm
        data = {
        'form': form
    }
        return render(request, 'main/profile.html', data)
    else:
        return redirect('index')

