from ..types.irma_type import IrmaType
from ..models import Irma
import graphene
from graphql_jwt.decorators import login_required


class IrmaQuery(graphene.ObjectType):
    irma = graphene.List(IrmaType)

    @login_required
    def resolve_irma(self, info):
        irma = Irma.objects.all()
        return irma
