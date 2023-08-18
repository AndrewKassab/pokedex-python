from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer

POKEMON_VIEW_ENDPOINT = '/pokemon/api/'
POKEMON_VIEW_ID_ENDPOINT = POKEMON_VIEW_ENDPOINT + "{id}/"

# Create your tests here.
class PokemonApiViewTest(APiTestCase):

    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'pokemon_types.json') #TODO: CREATE FIXTURE
        call_command('loaddata', 'test_pokemon.json') #TODO: CREATE FIXTURE

    def extract_list_from_response(self, data_list):
        seralializer = PokemonSerializer(data=data_list, many=True)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def test_get_all_pokemon(self):
        response = self.client.get(POKEMON_VIEW_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_list = self.extract_list_from_response(response.data)
        self.assertEqual(len(data_list), 10)

    def test_get_pokemon_by_id(self):
        response = self.client.get(POKEMON_VIEW_ID_ENDPOINT.format(id=1))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_list = self.extract_list_from_response(response.data)
        self.assertEqual(len(data_list), 1)


