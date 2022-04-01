from ..types.coalition_metric_type import CoalitionMetricType
from ..models import CoalitionsMetrics
import graphene
from graphql_jwt.decorators import login_required


class CoalitionMetricQuery(graphene.ObjectType):
    coalition_metric = graphene.List(CoalitionMetricType)

    @login_required
    def resolve_coalition_metric(self, info):
        coalition_metric = CoalitionsMetrics.objects.all()
        return coalition_metric
