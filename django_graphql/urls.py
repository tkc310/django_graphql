from django.conf.urls import include, url
from django.contrib import admin
from graphene_django.views import GraphQLView


urlpatterns = [
    url(r'^graphql/', GraphQLView.as_view(graphiql=True)),  # <- graphql_sample
    url(r'^admin/', admin.site.urls),
]
