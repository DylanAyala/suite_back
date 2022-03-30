from ..models import Campaign
from graphene_django import DjangoObjectType


class CampaingType(DjangoObjectType):
    class Meta:
        model = Campaign
