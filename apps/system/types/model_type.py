from ..models import Module
from graphene_django import DjangoObjectType


class ModuleType(DjangoObjectType):
    class Meta:
        model = Module
