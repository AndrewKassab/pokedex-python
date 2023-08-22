from django.core.management import call_command
from rest_framework.test import APITestCase
from rest_framework import status

POKEMON_VIEW_ENDPOINT = '/pokemon/api/'
POKEMON_VIEW_ID_ENDPOINT = POKEMON_VIEW_ENDPOINT + "{id}/"

# Create your tests here.
class PokemonApiViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'pokemon/fixtures/pokemontype_fixture.json')
        call_command('loaddata', 'pokemon/tests/fixtures/test_pokemon_fixture.json')

    def test_get_all_pokemon(self):
        response = self.client.get(POKEMON_VIEW_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_get_pokemon_by_id(self):
        response = self.client.get(POKEMON_VIEW_ID_ENDPOINT.format(id=1))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Bulbasaur')

    def test_get_pokemon_by_type(self):
        response = self.client.get(POKEMON_VIEW_ENDPOINT + "?type=Fire")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_pokemon_not_found(self):
        response = self.client.get(POKEMON_VIEW_ID_ENDPOINT.format(id=0))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_pokemon(self):
        data= {
            'id': '2',
            'name': 'Ivysaur',
            'primary_type': 'Grass',
        }
        response = self.client.post(POKEMON_VIEW_ENDPOINT, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Ivysaur')

    def test_create_pokemon_existing_fields(self):
        data = {
            'id': '1',
            'name': 'Bulbasaur',
            'primary_type': 'Grass',
        }
        response = self.client.post(POKEMON_VIEW_ENDPOINT, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['name'][0]), "pokemon with this name already exists.")
        self.assertEqual(str(response.data['id'][0]), "pokemon with this id already exists.")

    def test_create_pokemon_bad_type(self):
        data = {
            'id': '12',
            'name': 'New Pokemon',
            'primary_type': 'Fake type',
        }
        response = self.client.post(POKEMON_VIEW_ENDPOINT, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNotNone(response.data['primary_type'])

    def test_delete_pokemon(self):
        response = self.client.delete(POKEMON_VIEW_ID_ENDPOINT.format(id=1))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_pokemon_not_found(self):
        response = self.client.delete(POKEMON_VIEW_ID_ENDPOINT.format(id=0))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_pokemon(self):
        new_id = 20
        new_name = 'Bublee'
        data = {
            'id': new_id,
            'name': new_name,
            'primary_type': 'Grass',
        }
        response = self.client.put(POKEMON_VIEW_ID_ENDPOINT.format(id=1), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], new_name)
        self.assertEqual(response.data['id'], new_id)

    def test_update_pokemon_invalid_type(self):
        data = {
            'id': '1',
            'name': 'Bulbasaur',
            'primary_type': 'Fake type',
        }
        response = self.client.put(POKEMON_VIEW_ID_ENDPOINT.format(id=1), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)





