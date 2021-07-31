from django.conf.urls import include, url
from django.contrib import admin
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    url(r'^admin/', admin.site.urls),
]
