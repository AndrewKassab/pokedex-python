from django.views import generic
from pokedexapi.models import Pokemon


class ListView(generic.ListView):
    template_name = 'pokedexweb/index.html'
    model = Pokemon
    queryset = Pokemon.objects.all().order_by('id')
    context_object_name = 'pokemons'


class DetailView(generic.DetailView):
    template_name = 'pokedexweb/detail.html'
    model = Pokemon
    