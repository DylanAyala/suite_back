from ..types.paths_metrics_type import PathMetricsType
from ..models import PathsMetrics
import graphene
from graphql_jwt.decorators import login_required


class PathsMetricsQuery(graphene.ObjectType):
    paths_metrics = graphene.List(PathMetricsType)

    @login_required
    def resolve_paths_metrics(self, info):
        paths_metrics = PathsMetrics.objects.all()
        return paths_metrics
