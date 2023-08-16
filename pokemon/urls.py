from django.urls import path
from pokemon.views.pokemonapiview import *

app_name = 'pokemon'
urlpatterns = [
    path('pokemon/', PokemonAPIView.as_view(), name='pokemon'),
    path('pokemon/<int:pk>/', PokemonDetailAPIView.as_view(), name='pokemon-detail')
]