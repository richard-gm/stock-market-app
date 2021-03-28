from django.contrib import admin

# Register your models here.

from .models import Tweet


# admin model fields can be added below
class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['user__username', 'user__email']

    class Meta:
        model = Tweet


# Every class that you add need to be added below
admin.site.register(Tweet, TweetAdmin)
