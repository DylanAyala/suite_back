from ..models import Irma
from graphene_django import DjangoObjectType


class IrmaType(DjangoObjectType):
    class Meta:
        model = Irma
