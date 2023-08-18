from django.urls import path
from pokemon.views.pokemonapiview import PokemonListApiView, PokemonDetailApiView

app_name = 'pokemon'
urlpatterns = [
    path('api/', PokemonListApiView.as_view(), name='pokemon'),
    path('api/<int:pk>/', PokemonDetailApiView.as_view(), name='pokemon-detail')
]