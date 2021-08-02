import graphene
import items.schema
import posts.schema


class Query(items.schema.Query,
    posts.schema.Query,
    graphene.ObjectType):
    pass

class Mutation(items.schema.Mutation,
    posts.schema.Mutation,
    graphene.ObjectType):
    pass

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
