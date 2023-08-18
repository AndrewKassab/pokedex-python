from django.core.validators import RegexValidator
from django.db import models

color_regex = RegexValidator(
    regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
    message="Color code must be in the format #RRGGBB or #RGB."
)

class PokemonType(models.Model):
    name = models.CharField(max_length=20, primary_key = True)
    color = models.CharField(max_length=7, validators=[color_regex])
    weak_against = models.ManyToManyField('self', related_name='+', blank=True, symmetrical=False)
    immune_against = models.ManyToManyField('self', related_name='+', blank=True, symmetrical=False)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False, blank=False)
    name = models.CharField(max_length=30, unique=True)
    primary_type = models.ForeignKey('PokemonType', related_name='+', on_delete=models.CASCADE)
    secondary_type = models.ForeignKey('PokemonType', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    @property
    def weaknesses(self):
        primary_type_weaknesses = set(self.primary_type.weak_against.all())
        secondary_type_weaknesses = set(self.secondary_type.weak_against.all()) if self.secondary_type else set()

        total_weaknesses = primary_type_weaknesses | secondary_type_weaknesses

        primary_type_immunities = set(self.primary_type.immune_against.all())
        secondary_type_immunities = set(self.secondary_type.immune_against.all()) if self.secondary_type else set()

        total_immunities = primary_type_immunities | secondary_type_immunities

        final_weaknesses = total_weaknesses - total_immunities
        return list(final_weaknesses)

    def __str__(self):
        return self.name
