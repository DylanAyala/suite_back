from ..types.path_analisis_touchpoint_type import PathAnalisisTouchpointType
from ..models import PathAnalisisTouchpoint
import graphene
from graphql_jwt.decorators import login_required


class PathAnalisisTouchpointQuery(graphene.ObjectType):
    path_analisis_touchpoint = graphene.List(PathAnalisisTouchpointType)

    @login_required
    def resolve_path_analisis_touchpoint(self, info):
        path_analisis_touchpoint = PathAnalisisTouchpoint.objects.all()
        return path_analisis_touchpoint
