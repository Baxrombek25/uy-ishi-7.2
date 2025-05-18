from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrSuperUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return obj.owner == request.user or request.user.is_superuser
