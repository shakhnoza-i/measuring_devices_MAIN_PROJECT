from rest_framework import permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http.response import HttpResponse
from django.apps import apps
from accounts.models import Customer
from rest_framework import filters


class IsCustomer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        full_owners = obj.full_owner
        part_owners = obj.part_owner

        if obj.owner == request.user or request.user.is_staff:
            return True
        elif full_owners is not None:
            for i in full_owners:
                if i == request.user.username:
                    return True
        # elif part_owners is not None and request.method == "GET":
        elif part_owners is not None and request.method in permissions.SAFE_METHODS:
            for i in part_owners:
                if i == request.user.username:
                    return True
        else:
            return False
        #return obj.owner == request.user or request.user.is_staff
