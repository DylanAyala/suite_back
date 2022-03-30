from ..models import Channel
from graphene_django import DjangoObjectType


class ChannelType(DjangoObjectType):
    class Meta:
        model = Channel
