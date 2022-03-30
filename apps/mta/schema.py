
import graphene
from .queries.convertion_type_query import ConversionTypeQuery
from .queries.convertion_group_query import ConversionGroupQuery
from .queries.target_group_query import TargetGroupeQuery
from .queries.mta_result_query import MtaResultQuery
from .queries.path_metrics_query import PathsMetricsQuery
from .queries.path_analisis_touchpoint_query import PathAnalisisTouchpointQuery
from .queries.path_analisis_channel_query import PathAnalisisChannelQuery


class Query(ConversionTypeQuery, ConversionGroupQuery, TargetGroupeQuery, MtaResultQuery, PathsMetricsQuery, PathAnalisisTouchpointQuery, PathAnalisisChannelQuery):
    pass


class Mutation(graphene.ObjectType):
    pass
