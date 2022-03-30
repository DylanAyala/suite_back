from ..types.channel_type import ChannelType
from ..models import Channel
import graphene
from graphql_jwt.decorators import login_required


class ChannelQuery(graphene.ObjectType):
    channel = graphene.List(ChannelType)

    @login_required
    def resolve_channel(self, info):
        channel = Channel.objects.all()
        return channel
