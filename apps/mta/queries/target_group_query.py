from ..types.target_group_type import TargetGroupType
from ..models import TargetGroupConversion
import graphene
from graphql_jwt.decorators import login_required


class TargetGroupeQuery(graphene.ObjectType):
    target_group = graphene.List(TargetGroupType)

    @login_required
    def resolve_target_group(self, info):
        target_group = TargetGroupConversion.objects.all()
        return target_group
