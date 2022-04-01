from ..models import CampaingType
from graphene_django import DjangoObjectType


class CampaingTypeType(DjangoObjectType):
    class Meta:
        model = CampaingType
