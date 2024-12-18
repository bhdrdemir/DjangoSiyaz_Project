from django.urls import path
from django.urls.conf import include
from . import views
from graphene_django.views import GraphQLView
from items.schema import schema

urlpatterns = [

    path('', views.test, name="test"),

    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),

]