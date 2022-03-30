from ..types.conversion_type_type import ConversionTypeType
from ..models import ConversionType
import graphene
from graphql_jwt.decorators import login_required


class ConversionTypeQuery(graphene.ObjectType):
    conversion_type = graphene.List(ConversionTypeType)

    @login_required
    def resolve_conversion_type(self, info):
        conversion_type = ConversionType.objects.all()
        return conversion_type
