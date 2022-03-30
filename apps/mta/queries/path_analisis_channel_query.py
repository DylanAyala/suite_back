from ..types.path_analisis_channel_type import PathAnalisisChannelType
from ..models import PathAnalisisChannel
import graphene
from graphql_jwt.decorators import login_required


class PathAnalisisChannelQuery(graphene.ObjectType):
    path_analisis_channel = graphene.List(PathAnalisisChannelType)

    @login_required
    def resolve_path_analisis_channel(self, info):
        path_analisis_channel = PathAnalisisChannel.objects.all()
        return path_analisis_channel
