from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

User = get_user_model()

class UserType(DjangoObjectType):
    class Meta:
        model = User
       # exclude = ('password', ) # we can also exclude password or any other attribute we like not to see 