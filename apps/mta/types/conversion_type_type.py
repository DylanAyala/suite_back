from ..models import ConversionType
from graphene_django import DjangoObjectType


class ConversionTypeType(DjangoObjectType):
    class Meta:
        model = ConversionType
