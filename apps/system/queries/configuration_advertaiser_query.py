from ..types.configuration_advertaiser_type import ConfigurationAdvertaiserType
from ..models import ConfigruationAdvertiser
import graphene
from graphql_jwt.decorators import login_required


class ConfigurationAdvertaiserQuery(graphene.ObjectType):
    configuration_advertaiser = graphene.List(ConfigurationAdvertaiserType)

    @login_required
    def resolve_configuration_advertaiser(self, info):
        configuration_advertaiser = ConfigruationAdvertiser.objects.all()
        return configuration_advertaiser
