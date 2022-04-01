from ..types.campaing_category_type import CampaingCategoryType
from ..models import CampaingCategory
import graphene
from graphql_jwt.decorators import login_required


class CampaingCategoryQuery(graphene.ObjectType):
    campaing_category = graphene.List(CampaingCategoryType)

    @login_required
    def resolve_campaing_category(self, info):
        campaing_category = CampaingCategory.objects.all()
        return campaing_category
