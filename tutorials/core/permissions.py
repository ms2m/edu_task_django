from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # print('aaaaaa..   ... {} ... {}'.format(obj, dir(obj)))
        # print('object user: {} \t requested user... {}\n\n'.format(obj.user, request.user))
        # print(request.method , permissions.SAFE_METHODS)
        # if request.method in permissions.SAFE_METHODS:
            # pass
        return obj.user == request.user
