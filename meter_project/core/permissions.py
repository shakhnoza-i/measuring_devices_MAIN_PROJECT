from rest_framework import permissions


class IsOwnerOrGrantedUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
      
        return obj.creater == request.user or request.user.is_staff  # or obj.granted_user == request.user