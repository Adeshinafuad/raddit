from .models import Post, Vote
from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import PostSerializers,VoteSerializers

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
        
class PostRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(pk = kwargs['pk'], author=self.request.user)
        if post.exists():
            return self.destroy(request, *args,**kwargs)
        else:
            raise ValidationError("You are not the author of this post")
        
    
        
        
class VoteCreateView(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializers
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk = self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)
    
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError("User have already up voted")
        
        
        serializer.save(voter = self.request.user, post = Post.objects.get(pk = self.kwargs['pk']))
        
    
    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            raise ValidationError("You never voted")
        

        
    
        