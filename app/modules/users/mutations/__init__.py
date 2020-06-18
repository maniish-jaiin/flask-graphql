from graphene import AbstractType

from .RegisterUser import RegisterUser


class UserMutation(AbstractType):
    register_user = RegisterUser.Field()
