from ..types.mta_result_type import MtaResultType
from ..models import MtaResult
import graphene
from graphql_jwt.decorators import login_required


class MtaResultQuery(graphene.ObjectType):
    mta_result = graphene.List(MtaResultType)

    @login_required
    def resolve_mta_result(self, info):
        mta_result = MtaResult.objects.all()[:10]
        return mta_result
