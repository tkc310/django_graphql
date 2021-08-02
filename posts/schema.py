import graphene
from graphene_django import DjangoObjectType
from posts.models import Post as PostModel


class Post(DjangoObjectType):
    class Meta:
        model = PostModel

class Query(graphene.ObjectType):
    posts = graphene.List(Post)

    def resolve_posts(self, info, **kwargs):
        return PostModel.objects.all()

class CreatePost(graphene.Mutation):
    post = graphene.Field(lambda :Post)

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    def mutate(self, info, title, content):
        post = PostModel.objects.create(title=title, content=content)
        return CreatePost(post=post)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
