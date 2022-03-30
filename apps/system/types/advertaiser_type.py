from ..models import Advertiser
from graphene_django import DjangoObjectType


class AdvertaiserType(DjangoObjectType):
    class Meta:
        model = Advertiser
