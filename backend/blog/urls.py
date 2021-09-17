from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView #importing  React Tempalates
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',TemplateView.as_view(template_name='index.html')),#for react but did not work for me// may be I don't know
    path('', include('posts.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))), #Graphql
]
