from app.graphql.queries import (
    user_query,
    group_query,
    trip_query,
    destination_query,
    activity_query
)
from app.graphql.mutations import (
    user_mutation,
    group_mutation,
    trip_mutation,
    destination_mutation,
    activity_mutation
)

from strawberry import Schema
from strawberry.tools import merge_types
from strawberry.fastapi import GraphQLRouter

query = merge_types("Query", (
    user_query.UserQuery,
    group_query.GroupQuery,
    trip_query.TripQuery,
    destination_query.DestinationQuery,
    activity_query.ActivityQuery
))

# class Mutation(
#     user_mutation.UserMutation,
#     group_mutation.GroupMutation,
#     trip_mutation.TripMutation,
#     destination_mutation.DestinationMutation,
#     activity_mutation.ActivityMutation
# ):
#     pass
# schema = Schema(query=query, mutation=Mutation)


schema = Schema(query=query)

graphql_router = GraphQLRouter(schema=schema)