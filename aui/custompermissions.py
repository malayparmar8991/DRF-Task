from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAdminUser

class MyPermissions():
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in ['Staff']:
                if request.method == 'GET':
                    return True
            elif group in ['Manager']:
                return True
            elif IsAdminUser:
                return True
            return False
    def has_object_permission(self, request, view, obj):
        return True

class MyObjPermissions():
    def has_permission(self, request, view):
        return True
    def has_object_permission(self, request, view, obj):
        return True