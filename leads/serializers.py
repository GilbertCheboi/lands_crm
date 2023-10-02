from email.mime import image
from django.conf import settings
from rest_framework import serializers
from profiles.serializers import PublicProfileSerializer
from .models import Tweet
from django.contrib.humanize.templatetags.humanize import naturaltime



class TweetCreateSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    
    class Meta:
        model = Tweet
        fields = ['user',
                  'property', 
                  'id', 
                  'description', 
                  'lead',
                  'agent',
                  'amount', 
                  'due_date',
                  'payment_staus',
                  'mode_of_payment']

 



class TweetSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True)

    class Meta:
        model = Tweet
        fields = [
                'user', 
                'id', 
                'property',
                'description',
                'lead',
                'agent',
                'amount',
                'payment_status',
                'mode_of_payment',
                'timestamp',
                'due_date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['timestamp'] = naturaltime(instance.timestamp)
        return representation


