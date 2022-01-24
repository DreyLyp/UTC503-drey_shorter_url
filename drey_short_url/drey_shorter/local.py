from django.urls import path
from . import views

# This allows us to define the patern for our urls in order to perform our various actions
# such as creating or redirecting a link
urlpatterns = [
    path('', views.index),
    path('create', views.create_shorter_url, name='create'),
    path('<str:pk>', views.redirect_to_real_link)
]