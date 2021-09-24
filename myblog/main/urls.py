from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog),
    path('404', error404, name='404'),
    path('blog/<slug:post_slug>/', show_article),
    path('registernewuser/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view()),
    path('accounts/profile/', profile)
]