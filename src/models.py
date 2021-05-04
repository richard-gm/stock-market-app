import random
from django.db import models
from django.conf import settings
from django.db.models import Q
User = settings.AUTH_USER_MODEL
# Create your models here. (models are equal to tables in django)


# table for likes of each tweet
# Watch tutorial from 3h50min onwards
class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class TweetComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class TweetQuerySet(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)

    def feed(self, user):
        profile_exist = user.following.exists()
        followed_users_id = []
        if profile_exist:
            followed_users_id = user.following.values_list("user__id", flat=True)
        return self.filter(
            Q(user__id__in=followed_users_id) |
            Q(user=user)
        ).distinct().order_by("-timestamp")  # adding a - give us newest first


class TweetManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return TweetQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)


# table for content of each tweet
class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")  # One user only
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)  # List of users | can also be applied for comments etc
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TweetManager()

    class Meta:
        ordering = ['-id']

    @property   # 4h 37min
    def is_retweet(self):
        return self.parent != None #if the parent is equal to none then is a retweet (bolan)

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }
