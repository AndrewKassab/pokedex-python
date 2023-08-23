from django.urls import path
from pokedexweb.views import DetailView, ListView

urlpatterns = [
    path('', ListView.as_view(), name='index'),
    path('<int:pk>', DetailView.as_view(), name='detail')
]