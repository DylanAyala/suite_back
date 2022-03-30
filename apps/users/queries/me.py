from ..types.user_type import UserType
from ..models import User
import graphene


class MeQuery(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('!Not logged in! Try again')
        return user
