from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# model for Post
class Post(models.Model):
    title  = models.CharField(max_length=255)
    body   = models.TextField()
    poster = models.ForeignKey(User,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


# model for Vote
class Vote(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    voter=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.voter} -> {self.post}"