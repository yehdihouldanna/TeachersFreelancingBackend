from rest_framework import permissions

# class IsAdminOrReadOnly(permissions.IsAdminUser):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             # Check permissions for read-only request
#             return True
#         else:
#             return bool(request.user and request.user.is_staff)



class IsTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try :
            return (obj.user == request.user) or (request.user and request.user.is_teacher)
        except:
            pass

        #for the order related objects :
        return (obj.user == request.user) or (request.user and request.user.is_teacher)
class IsCurrentUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try :
            return (obj.user == request.user) or (request.user and request.user.is_staff)
        except:
            pass

        #for the order related objects :
        return (obj.order.user == request.user) or (request.user and request.user.is_staff)