from ..types.campaing_type_type import CampaingTypeType
from ..models import CampaingType
import graphene
from graphql_jwt.decorators import login_required


class CampaingTypeQuery(graphene.ObjectType):
    campaing_type = graphene.List(CampaingTypeType)

    @login_required
    def resolve_campaing_type(self, info):
        campaing_type = CampaingType.objects.all()
        return campaing_type
