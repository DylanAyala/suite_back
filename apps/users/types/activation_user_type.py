import graphene


class ActivationUserType(graphene.ObjectType):
    status = graphene.Boolean()
    message = graphene.String()
