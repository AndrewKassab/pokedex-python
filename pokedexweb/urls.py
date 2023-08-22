from django.urls import path
from pokedexweb.views import DetailView

urlpatterns = [
    path('<int:pk>', DetailView.as_view(), name='detail')
]