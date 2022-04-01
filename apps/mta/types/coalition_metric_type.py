from ..models import CoalitionsMetrics
from graphene_django import DjangoObjectType


class CoalitionMetricType(DjangoObjectType):
    class Meta:
        model = CoalitionsMetrics
