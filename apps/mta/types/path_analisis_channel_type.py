from ..models import PathAnalisisChannel
from graphene_django import DjangoObjectType


class PathAnalisisChannelType(DjangoObjectType):
    class Meta:
        model = PathAnalisisChannel
