
from ..models import CampaingCategory
from graphene_django import DjangoObjectType


class CampaingCategoryType(DjangoObjectType):
    class Meta:
        model = CampaingCategory
