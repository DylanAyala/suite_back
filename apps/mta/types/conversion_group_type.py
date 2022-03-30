from ..models import ConversionGroup
from graphene_django import DjangoObjectType


class ConversionGroupType(DjangoObjectType):
    class Meta:
        model = ConversionGroup
