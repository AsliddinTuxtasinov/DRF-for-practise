from rest_framework import (
    generics,permissions,authentication,exceptions,
    mixins,response,status
)
from .models import Post, Vote
from .serializers import PostListSerializers, VoteSerializers



# Post list View
class PostListViews(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostListSerializers

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


# Post detail and delete view
class PostRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostListSerializers

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=kwargs["pk"], poster=request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise exceptions.ValidationError("Bu post sizning po'stingiz emas O'chirish uchun, BRUH!")


# Vote create and delete view
class VoteCreateview(generics.CreateAPIView,mixins.DestroyModelMixin):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = VoteSerializers

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user,post=post)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise exceptions.ValidationError("Siz allaqachon ovoz berib bo'lgansiz :)")
        serializer.save(post =Post.objects.get(pk=self.kwargs['pk']), voter=self.request.user)

    def delete(self,request,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise exceptions.ValidationError("Siz hali ovoz berganiz yo'q :(")