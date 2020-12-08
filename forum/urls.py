from django.urls import path

from forum.views import (
    new_post_view,
)

app_name = 'forum'

urlpatterns = [
    path('new-post/', new_post_view, name='new_post'),
]
