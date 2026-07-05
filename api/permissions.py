from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Any authenticated user (Scouts) can view (GET) the list.
    - Only users with the ADMIN role can create, edit, or delete.
    """
    def has_permission(self, request, view):
        # Allow GET, HEAD, or OPTIONS requests for any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        # Write permissions (POST, PUT, DELETE) are only allowed for Admins
        return request.user and request.user.role == 'ADMIN'