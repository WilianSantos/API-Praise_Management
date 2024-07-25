# no seu_app_de_usuario/permissions.py
from rest_framework.permissions import BasePermission

class AllowAnyPost(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated
