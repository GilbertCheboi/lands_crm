from urllib import request
from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Profile, ChampionLeague, AfconLeague, Baseball, Bundesliga, Formula1, Laliga, NBA, NFL, Worldcup
from tweets.models import Tweet
#from tweets.serializers import TweetSerializer
#from accounts.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    location = serializers.CharField(required=False)
    First_Name = serializers.CharField(required=False)
    Last_Name = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    clubimage = serializers.ImageField(required=False)
    Team1 = serializers.ImageField(required=False)
    Afcon = serializers.ImageField(required=False)
    Baseball = serializers.ImageField(required=False)
    Bundesliga = serializers.ImageField(required=False)
    Europa = serializers.ImageField(required=False)
    Formula1 = serializers.ImageField(required=False)
    Laliga = serializers.ImageField(required=False)
    NBA = serializers.ImageField(required=False)
    NFL = serializers.ImageField(required=False)
    Worldcup = serializers.ImageField(required=False)
    Team = serializers.ImageField(required=False)
    Team = serializers.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email',]


class ProfileSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(required=False)
    # last_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    username = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Profile
        fields = ['location', 'bio', 'First_Name','Last_Name','image', 'email', 'username','clubimage', 'Afcon', 'Baseball', 'Bundesliga', 'Europa','Formula1', 'Laliga', 'NBA', 'NFL', 'Worldcup']
    def get_username(self, obj):
        return obj.user.username

class ProfileBasicSerializer(serializers.Serializer):
    First_Name = serializers.CharField(required=False)
    Last_Name = serializers.CharField(required=False)
    email_address = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    location = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    clubimage = serializers.ImageField(required=False)



class PublicProfileSerializer(serializers.ModelSerializer):
    # first_name = serializers.SerializerMethodField(read_only=True)
    # last_name = serializers.SerializerMethodField(read_only=True)
    is_following = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    #feed = serializers.SerializerMethodField(read_only=True)
    follower_count = serializers.SerializerMethodField(read_only=True)
    following_count = serializers.SerializerMethodField(read_only=True)
    Afcon = serializers.ImageField(source='Afcon.icon')
    Baseball = serializers.ImageField(source='Baseball.icon')
    Bundesliga = serializers.ImageField(source='Bundesliga.icon')
    Europa = serializers.ImageField(source='Europa.icon')
    Formula1 = serializers.ImageField(source='Formula1.icon')
    Laliga = serializers.ImageField(source='Laliga.icon')
    NBA = serializers.ImageField(source='NBA.icon')
    NFL = serializers.ImageField(source='NFL.icon')
    Worldcup = serializers.ImageField(source='Worldcup.icon')

    class Meta:
        model = Profile
        fields = [
            "First_Name",
            "Last_Name",
            "id",
            "image",
            "Afcon",
            "Baseball",
            "Bundesliga",
            "Europa",
            "Formula1",
            "Laliga",
            "NBA",
            "NFL",
            "Worldcup",
            "bio",
            "location",
            "follower_count",
            "following_count",
            "is_following",
            "username",
        ]
    
    def get_is_following(self, obj):
        # request???
        is_following = False
        context = self.context
        request = context.get("request")
        if request:
            user = request.user
            is_following = user in obj.followers.all()
        return is_following
    
    def get_first_name(self, obj):
        return obj.user.first_name
    
   
    def get_last_name(self, obj):
        return obj.user.last_name
    
    def get_username(self, obj):
        return obj.user.username
        
    # def get_feed(obj):
    #     qs = Tweet.objects.all(obj)
    #     feed = TweetSerializer(qs, request)
    #     return feed
    
    def get_following_count(self, obj):
        return obj.user.following.count()
    
    def get_follower_count(self, obj):
        return obj.followers.count()

