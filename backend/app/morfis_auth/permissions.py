from rest_framework import permissions


class IsSubdivisionMember(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # print(vars(request.user.subdivision))
        # print(vars(obj.subdivision))

        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # Instance must have an attribute named `owner`.
        # return obj.owner == request.user
        # return True

        if request.user.subdivision == obj.subdivision:
            return True

        return False