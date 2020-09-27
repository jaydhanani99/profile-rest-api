from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # Safe methods are the methods which not modify the data however it can read data
        # so in our case one user can read other user info but cannot edit
        if request.method in permissions.SAFE_METHODS:
            return True

        # obj id is the actually model id of current user
        return obj.id == request.user.id


