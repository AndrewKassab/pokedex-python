from django.views import generic
from pokedexapi.models import Pokemon


class ListView(generic.ListView):
    template_name = 'pokedexweb/index.html'
    model = Pokemon

    def get_queryset(self):
        return Pokemon.objects.all()


class DetailView(generic.DetailView):
    template_name = 'pokedexweb/detail.html'
    model = Pokemon
    