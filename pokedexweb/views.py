from django.shortcuts import render
from django.views import generic
from pokedexapi.models import Pokemon

# Create your views here.
class DetailView(generic.DetailView):
    template_name = 'pokedexweb/detail.html'
    model = Pokemon
    