from ..models import Investment
from graphene_django import DjangoObjectType


class InvestmentType(DjangoObjectType):
    class Meta:
        model = Investment
