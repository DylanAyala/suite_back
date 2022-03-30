import graphene
from ..types.activation_user_type import ActivationUserType
from ..models import User, Group
from graphql_jwt.decorators import login_required, permission_required


class ActivationUserMutation(graphene.Mutation):
    status = graphene.Field(ActivationUserType)

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        user = User.objects.filter(id=id)
        user.update(is_active=True)
        change = ActivationUserType(
            status=True, message="Se activo la cuenta correctamente")
        return ActivationUserMutation(status=change)
