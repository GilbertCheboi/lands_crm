from django.contrib import admin

# Register your models here.
from .models import Tweet




class TweetAdmin(admin.ModelAdmin):

    class Meta:
        model = Tweet







admin.site.register(Tweet, TweetAdmin)




# Register your models here.
