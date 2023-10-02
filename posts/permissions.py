from rest_framework import permissions

class isAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True 
        return False 
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True 

        # Write permissions are only allowed to the author of a post
        return obj.author == request.user 