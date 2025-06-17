import graphene
import event.schema as event_schema

class Query(event_schema.Query, graphene.ObjectType):
    ...

class Mutation(event_schema.Mutation, graphene.ObjectType):
    ...

schema = graphene.Schema(query=Query, mutation=Mutation)