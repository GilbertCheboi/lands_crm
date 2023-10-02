import random
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class TweetManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return TweetQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)




class Tweet(models.Model):
    property = models.TextField(blank=True, null=True)
    lead = models.TextField(blank=True, null=True)
    agent = models.TextField(blank=True, null=True)
    amount = models.TextField(blank=True, null=True)
    due_date = models.TextField(blank=True, null=True)
    payment_status = models.TextField(blank=True, null=True)
    mode_of_payment = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
   
    objects = TweetManager()