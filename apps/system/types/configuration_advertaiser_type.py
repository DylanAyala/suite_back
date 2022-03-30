from ..models import ConfigruationAdvertiser
from graphene_django import DjangoObjectType


class ConfigurationAdvertaiserType(DjangoObjectType):
    class Meta:
        model = ConfigruationAdvertiser
