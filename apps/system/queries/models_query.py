from ..types.model_type import ModuleType
from ..models import Module
import graphene
from graphql_jwt.decorators import login_required


class ModelQuery(graphene.ObjectType):
    modules = graphene.List(ModuleType)

    @login_required
    def resolve_modules(self, info):
        modules = Module.objects.all()
        return modules
