from ..models import PathsMetrics
from graphene_django import DjangoObjectType


class PathMetricsType(DjangoObjectType):
    class Meta:
        model = PathsMetrics
