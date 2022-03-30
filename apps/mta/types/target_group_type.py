from ..models import TargetGroupConversion
from graphene_django import DjangoObjectType


class TargetGroupType(DjangoObjectType):
    class Meta:
        model = TargetGroupConversion
