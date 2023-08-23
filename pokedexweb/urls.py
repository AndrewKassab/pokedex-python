from django.urls import path
from pokedexweb.views import DetailView, ListView

app_name = 'pokedexweb'

urlpatterns = [
    path('', ListView.as_view(), name='index'),
    path('<int:pk>', DetailView.as_view(), name='detail')
]