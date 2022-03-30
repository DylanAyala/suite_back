import graphene
from ..types.user_type import UserType
from graphene_django.forms.mutation import DjangoModelFormMutation
from ..forms.update_user_form import UpdateUserForm


class UpdateUserMutation(DjangoModelFormMutation):
    user = graphene.Field(UserType)

    class Meta:
        form_class = UpdateUserForm

    @classmethod
    def perform_mutate(cls, form, info):
        obj = form.save()
        kwargs = {cls._meta.return_field_name: obj}
        return cls(errors=[], **kwargs)
