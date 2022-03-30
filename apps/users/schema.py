import graphene
from .queries.me import MeQuery
from .mutations.json_web_token import ObtainJSONWebToken
from .mutations.register_user_mutation import RegisterUserMutation
from .mutations.activation_user_mutation import ActivationUserMutation
from .queries.group_query import GroupQuery
from .queries.countries_query import CountriesQuery
from .mutations.update_user_mutation import UpdateUserMutation


class Query(MeQuery, GroupQuery, CountriesQuery):
    pass


class Mutation(graphene.ObjectType):
    auth = ObtainJSONWebToken.Field()
    register_user = RegisterUserMutation.Field()
    activation_user = ActivationUserMutation.Field()
    update_user = UpdateUserMutation.Field()
