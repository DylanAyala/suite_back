from ..types.advertaiser_type import AdvertaiserType
from ..models import Advertiser
import graphene
from graphql_jwt.decorators import login_required


class AdvertaiserQuery(graphene.ObjectType):
    advertaiser = graphene.List(AdvertaiserType)

    @login_required
    def resolve_advertaiser(self, info):
        advertaiser = Advertiser.objects.all()
        return advertaiser
