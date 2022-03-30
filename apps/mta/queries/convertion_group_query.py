from ..types.conversion_group_type import ConversionGroupType
from ..models import ConversionGroup
import graphene
from graphql_jwt.decorators import login_required


class ConversionGroupQuery(graphene.ObjectType):
    conversion_group = graphene.List(ConversionGroupType)

    @login_required
    def resolve_conversion_group(self, info):
        conversion_group = ConversionGroup.objects.all()
        return conversion_group
