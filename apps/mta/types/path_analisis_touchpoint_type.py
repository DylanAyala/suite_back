from ..models import PathAnalisisTouchpoint
from graphene_django import DjangoObjectType


class PathAnalisisTouchpointType(DjangoObjectType):
    class Meta:
        model = PathAnalisisTouchpoint
