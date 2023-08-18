from rest_framework import serializers
from pokemon.models import Pokemon, PokemonType


class PokemonTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PokemonType
        fields = '__all__'


class PokemonSerializer(serializers.ModelSerializer):
    weaknesses = serializers.ListSerializer(child=PokemonTypeSerializer(), source='weaknesses')
    type_primary = serializers.PrimaryKeyRelatedField(queryset=PokemonType.objects.all())
    type_secondary = serializers.PrimaryKeyRelatedField(queryset=PokemonType.objects.all(), required=False)

    class Meta:
        model = Pokemon
        fields = ('__all__', 'weaknesses')
        read_only_fields = ['created_date', 'updated_date']


