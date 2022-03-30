from ..types.campaing_type import CampaingType
from ..models import Campaign
import graphene
from graphql_jwt.decorators import login_required


class CampaingQuery(graphene.ObjectType):
    campaing = graphene.List(CampaingType)

    @login_required
    def resolve_campaing(self, info):
        campaing = Campaign.objects.all()
        return campaing
