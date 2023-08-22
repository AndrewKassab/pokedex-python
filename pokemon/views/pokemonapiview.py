from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer

class PokemonListApiView(APIView):

    def get(self, request):
        pokemon = Pokemon.objects.all()

        type = request.query_params.get('type', None)

        if type:
            pokemon = pokemon.filter(primary_type=type) | pokemon.filter(secondary_type=type)

        serializer = PokemonSerializer(pokemon, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PokemonDetailApiView(APIView):

    def get_object(self, pk):
        try:
            return Pokemon.objects.get(pk=pk)
        except Pokemon.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pokemon = self.get_object(pk)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)

    def put(self, request, pk):
        pokemon = self.get_object(pk)
        serializer = PokemonSerializer(pokemon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pokemon = self.get_object(pk)
        pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
