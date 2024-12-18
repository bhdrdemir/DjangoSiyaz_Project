import graphene
from graphene_django import DjangoObjectType
from .models import Items


class ItemType(DjangoObjectType):
    class Meta:
        model = Items
        fields = ("id", "title", "excerpt")

class Query(graphene.ObjectType):
    all_items = graphene.List(ItemType)

    def resolve_all_items(root, info):
        return Items.objects.all()

schema = graphene.Schema(query=Query)