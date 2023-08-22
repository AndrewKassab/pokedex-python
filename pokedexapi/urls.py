from rest_framework.routers import DefaultRouter
from django.urls import path, include
from pokedexapi.views.pokedexapiview import PokemonViewSet

router = DefaultRouter()
router.register(r'', PokemonViewSet)

app_name = 'pokedexapi'

urlpatterns = [
    path('', include(router.urls))
]