from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post,Vote
User = get_user_model()



# Poster Serialaizers
class PosterSerializers(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id','username']


# PostList serializers
class PostListSerializers(serializers.ModelSerializer):
    poster = PosterSerializers(read_only=True)
    votes = serializers.SerializerMethodField()
    class Meta:
        model  = Post
        fields = '__all__'

    def get_votes(self,post):
        return Vote.objects.filter(post=post).count()


# Vote serializers
class VoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields=['id']