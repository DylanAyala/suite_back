
import graphene

from mta.queries.campaing_type_query import CampaingTypeQuery
from .queries.convertion_type_query import ConversionTypeQuery
from .queries.convertion_group_query import ConversionGroupQuery
from .queries.target_group_query import TargetGroupeQuery
from .queries.mta_result_query import MtaResultQuery
from .queries.path_metrics_query import PathsMetricsQuery
from .queries.path_analisis_touchpoint_query import PathAnalisisTouchpointQuery
from .queries.path_analisis_channel_query import PathAnalisisChannelQuery
from .queries.irma_query import IrmaQuery
from .queries.investment_query import InvestmentQuery
from .queries.coalition_metric_query import CoalitionMetricQuery
from .queries.campaing_category_query import CampaingCategoryQuery


class Query(ConversionTypeQuery,
            ConversionGroupQuery,
            TargetGroupeQuery,
            MtaResultQuery,
            PathsMetricsQuery,
            PathAnalisisTouchpointQuery,
            PathAnalisisChannelQuery,
            IrmaQuery,
            InvestmentQuery,
            CoalitionMetricQuery,
            CampaingTypeQuery,
            CampaingCategoryQuery,):
    pass


class Mutation(graphene.ObjectType):
    pass
