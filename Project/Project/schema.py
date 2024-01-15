import graphene

from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

class AutoMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()

class Query(UserQuery, graphene.ObjectType):
    pass

class Mutation(AutoMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)