from django.urls import path
from .views import (
    tweets_action_view,
    tweets_delete_view,
    tweets_detail_view,
    tweets_list_view,
    create_post_view,
    tweet_feed_view,
)
'''
Client Side
Base ENDPOINT /profile/api/tweets
'''
urlpatterns = [
    path('', tweets_list_view),
    path('feed/', tweet_feed_view),
    path('action/', tweets_action_view),
    path('create/', create_post_view),
    path('<int:tweet_id>/', tweets_detail_view),
    path('<int:tweet_id>/delete/', tweets_delete_view),
]
