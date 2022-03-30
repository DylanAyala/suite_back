import imp
from re import I
import graphene
from .queries.models_query import ModelQuery
from .queries.advertaiser_query import AdvertaiserQuery
from .queries.configuration_advertaiser_query import ConfigurationAdvertaiserQuery
from .queries.channel_query import ChannelQuery
from .queries.campaing_query import CampaingQuery


class Query(ModelQuery, AdvertaiserQuery, ConfigurationAdvertaiserQuery, ChannelQuery, CampaingQuery):
    pass


class Mutation(graphene.ObjectType):
    pass
