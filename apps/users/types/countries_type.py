from ..models import Countries
from graphene_django import DjangoObjectType


class CountriesType(DjangoObjectType):
    class Meta:
        model = Countries
