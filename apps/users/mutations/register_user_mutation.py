import graphene
from ..models_all.user import User
from ..types.user_type import UserType
from graphene_django.forms.mutation import DjangoModelFormMutation
from ..forms.register_user_form import RegisterUserForm
from django.core.mail import EmailMessage
from suite_back.settings import SENDER_MAIL, SECRET_KEY
import jwt
import datetime


class RegisterUserMutation(DjangoModelFormMutation):
    user = graphene.Field(UserType)

    class Meta:
        form_class = RegisterUserForm

    @classmethod
    def perform_mutate(cls, form, info):
        obj = form.save()
        if form.data['email']:
            user = User.objects.filter(email=form.data['email'])
            date = datetime.datetime.today() + datetime.timedelta(days=1)
            token = ""
            for x in user:
                token = jwt.encode(
                    {'id': x.id, 'username': x.username,
                     'exp': date, 'origIat': 1581531746},
                    SECRET_KEY,
                    algorithm='HS256'
                ).decode('utf-8')
            mail = EmailMessage(subject="test", body="http://localhost:8080/" + token,
                                from_email=SENDER_MAIL, to=[form.data['email']])
            mail.content_subtype = "html"
            mail.send()

        kwargs = {cls._meta.return_field_name: obj}
        return cls(errors=[], **kwargs)
