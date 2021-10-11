from rest_framework import permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http.response import HttpResponse
from django.apps import apps
from accounts.models import Customer


class IsCustomer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        owners = obj.owner.all()
        for i in owners:
            if i == request.user:
                return True

        #return obj.owner == request.user or request.user.is_staff
