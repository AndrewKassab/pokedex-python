from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pokemon.models import Pokemon

class PokemonListApiView(APIView):

    def get(self, request):
        pokemon = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemon, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'name': request.date.get('name'),
            'type': request.date.get('type'),

        }
