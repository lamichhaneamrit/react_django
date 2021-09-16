
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),# content from admin panel
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))), #Graphql
]
