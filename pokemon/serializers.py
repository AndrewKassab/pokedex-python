from rest_framework import serializers
from pokemon.models import Pokemon, PokemonType


class PokemonTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PokemonType
        fields = '__all__'


# TODO: Type is currently case sensitive
class PokemonSerializer(serializers.ModelSerializer):
    weaknesses = serializers.ListSerializer(child=PokemonTypeSerializer(), required = False)
    primary_type = serializers.PrimaryKeyRelatedField(queryset=PokemonType.objects.all())
    secondary_type = serializers.PrimaryKeyRelatedField(queryset=PokemonType.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'primary_type', 'secondary_type', 'created_date', 'updated_date', 'weaknesses')
        read_only_fields = ['created_date', 'updated_date']


