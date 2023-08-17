from rest_framework import serializers
from pokemon.models import Pokemon, PokemonType

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('__all__', 'weaknesses')
        read_only_fields = ['created_date', 'updated_date']


class PokemonTypeSerializer(serializers.ModelSerializer):
    weaknesses = serializers.ListSerializer(child=PokemonTypeSerializer(), source='weaknesses')

    class Meta:
        model = PokemonType
        fields = '__all__'
