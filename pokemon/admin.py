from django.contrib import admin
from pokemon.models import PokemonType, Pokemon

admin.site.register(PokemonType)
admin.site.register(Pokemon)
