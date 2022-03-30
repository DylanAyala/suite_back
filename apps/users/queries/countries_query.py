from ..types.countries_type import CountriesType
from ..models import Countries
import graphene
from graphql_jwt.decorators import login_required


class CountriesQuery(graphene.ObjectType):
    countries = graphene.List(CountriesType)

    @login_required
    def resolve_countries(self, info):
        countries = Countries.objects.all()
        return countries
