import graphene
from graphene_django import DjangoObjectType
from items.models import Items


class Item(DjangoObjectType):
    class Meta:
        model = Items

class Query(graphene.ObjectType):
    items = graphene.List(Item)

    def resolve_items(self, info, **kwargs):
        return Items.objects.all()

class CreateItem(graphene.Mutation):
    item = graphene.Field(lambda :Item)

    class Arguments:
        name = graphene.String()
        count = graphene.Int()

    def mutate(self, info, name, count):
        item = Items.objects.create(name=name, count=count)
        return CreateItem(item=item)

class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()
