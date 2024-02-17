from rest_framework.permissions import BasePermission


class IsCompany(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_role == "CO"


class IsJobSeeker(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_role == "JS"


class DenyDuplicateProfile(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST" and request.user.user_role in ["CO", "JS"]:
            return False
        return True
