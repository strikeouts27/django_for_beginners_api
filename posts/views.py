from rest_framework import generics, permissions 
from .models import Post 
from .serializers import PostSerializer

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class BasePermission(object):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True