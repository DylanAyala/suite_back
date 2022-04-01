from ..types.investment_type import InvestmentType
from ..models import Investment
import graphene
from graphql_jwt.decorators import login_required


class InvestmentQuery(graphene.ObjectType):
    investment = graphene.List(InvestmentType)

    @login_required
    def resolve_investment(self, info):
        investment = Investment.objects.all()
        return investment
