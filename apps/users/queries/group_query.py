from ..types.group_type import GroupType
from ..models import Group
import graphene


class GroupQuery(graphene.ObjectType):
    group = graphene.List(GroupType)

    def resolve_group(self, info):
        group = Group.objects.all()
        return group
