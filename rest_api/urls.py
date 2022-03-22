from django.contrib import admin
from django.urls import re_path, path
from  rest_framework.urlpatterns import format_suffix_patterns

from rest_api import views
from views import index

post_list = index.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    # path('', views.index.as_view(), name="home")

    # re_path(r"^api/tutorials$", views.tutorial_list),
    # re_path(r"^api/tutorials/(?P<pk>[0-9]+)$", views.tutorial_detail),
    # re_path(r"^api/tutorials/published$", views.tutorial_list_published)

    path


])