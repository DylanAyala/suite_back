from ..models import MtaResult
from graphene_django import DjangoObjectType


class MtaResultType(DjangoObjectType):
    class Meta:
        model = MtaResult
