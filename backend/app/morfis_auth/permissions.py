from rest_framework import permissions


class IsHospitalMember(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

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
        if request.user.is_authenticated():
            return request.user.hospital == obj.hospital
        return False
