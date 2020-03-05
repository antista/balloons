from django.core.validators import MinValueValidator, RegexValidator
from django.db import models


class Entity(models.Model):
    name = models.CharField(max_length=100, primary_key=True, validators=[
        RegexValidator('^[a-z_]*$', 'Only lowercase letters and underscores allowed.')], )
    weight = models.IntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='static/styles/images/entities')

    @staticmethod
    def get_entities():
        return list(Entity.objects.filter())

    @staticmethod
    def get_entity(entity_name):
        return Entity.objects.filter(name=entity_name).first()
