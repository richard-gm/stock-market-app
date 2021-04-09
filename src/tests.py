# Create your tests here.

from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

from .models import Tweet

# We create a user so the Unit Test can perform the test
User = get_user_model()


# 4H50min Unit Testing setup
class TweetTestCase(TestCase):
    def setUp(self):  # DB data goes only here
        self.user = User.objects.create_user(username='Richard', password='somepassword')
        self.userb = User.objects.create_user(username='Andres', password='somepassword2')
        Tweet.objects.create(content="my first tweet - user 1",
                             user=self.user)
        Tweet.objects.create(content="my second tweet - user 1",
                             user=self.user)
        Tweet.objects.create(content="my first tweet - user 2",
                             user=self.userb)
        self.currentCount = Tweet.objects.all().count()  # counting how many tweets are

    def test_tweet_created(self):
        tweet_obj = Tweet.objects.create(content="my fourth tweet",
                                         user=self.user)
        self.assertEqual(tweet_obj.id, 4)
        self.assertEqual(tweet_obj.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/profile/api/tweets")  # Getting list of posts by user
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        print(response.json())

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/profile/api/tweets/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_action_like(self):
        client = self.get_client()
        response = client.post("/profile/api/tweets/action/",
                               {"id": 1, "action": "like"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 1)

    def test_action_unlike(self):
        client = self.get_client()
        response = client.post("/profile/api/tweets/action/",
                               {"id": 2, "action": "like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/profile/api/tweets/action/",
                               {"id": 2, "action": "unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 0)

    def test_action_retweet(self):
        client = self.get_client()
        response = client.post("/profile/api/tweets/action/",
                               {"id": 2, "action": "comment"})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_tweet_id = data.get("id")
        self.assertNotEqual(2, new_tweet_id)
        self.assertEqual(self.currentCount + 1, new_tweet_id)  # adding new tweet count

    def test_tweet_create_api_view(self):
        request_data = {"content": "This is my test tweet"}
        client = self.get_client()
        response = client.post("/profile/api/tweets/create/", request_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        new_tweet_id = response_data.get("id")
        self.assertEqual(self.currentCount + 1, new_tweet_id)

    def test_tweet_detail_api_view(self):
        client = self.get_client()
        response = client.get("/profile/api/tweets/3/")  # change the ID to test each post
        self.assertEqual(response.status_code, 200)
        data = response.json()
        _id = data.get("id")
        self.assertEqual(_id, 3)  # Post from DB have been deleted so ID id.1 is now id.3

    def test_tweet_delete_api_view(self):
        client = self.get_client()
        response = client.delete("/profile/api/tweets/1/delete/")
        self.assertEqual(response.status_code, 200)
        client = self.get_client()
        response = client.delete("/profile/api/tweets/1/delete/")
        self.assertEqual(response.status_code, 404)
        response_incorrect_owner = client.delete("/profile/api/tweets/3/delete/")
        self.assertEqual(response_incorrect_owner.status_code, 401)