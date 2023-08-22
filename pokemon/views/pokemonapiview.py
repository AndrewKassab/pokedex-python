from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer

class PokemonViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        type = self.request.query_params.get('type', None)

        if type:
            queryset = queryset.filter(primary_type=type) | queryset.filter(secondary_type=type)

        return queryset

    def retrieve(self, *args, **kwargs):
        instance = get_object_or_404(Pokemon, pk=kwargs['pk'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, *args, **kwargs):
        instance = get_object_or_404(Pokemon, pk=kwargs['pk'])
        serializer = self.get_serializer(instance, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, *args, **kwargs):
        instance = get_object_or_404(Pokemon, pk=kwargs['pk'])
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
