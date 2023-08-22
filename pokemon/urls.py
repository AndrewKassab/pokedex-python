from rest_framework.routers import DefaultRouter
from django.urls import path, include
from pokemon.views.pokemonapiview import PokemonViewSet

router = DefaultRouter()
router.register(r'api', PokemonViewSet)

app_name = 'pokemon'

urlpatterns = [
    path('', include(router.urls))
]