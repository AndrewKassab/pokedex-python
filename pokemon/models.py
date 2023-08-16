from django.db import models
from enum import Enum


class PokemonType(models.Model):
    name = models.CharField(max_length=15, unique=True)
    strong_against = models.ManyToManyField('self', related_name='+', blank=True, symmetrical=False)
    weak_against = models.ManyToManyField('self', related_name='+', blank=True, symmetrical=False)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False, blank=False)
    name = models.CharField(max_length=30, unique=True)
    primary_type = models.CharField(max_length=15, choices=[(pokemonType.value, pokemonType.name) for pokemonType in PokemonType])
    secondary_type = models.CharField(max_length=15, choices=[(pokemonType.value, pokemonType.name) for pokemonType in PokemonType], blank = True, null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
