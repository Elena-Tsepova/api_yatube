from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Позволяет редактировать объект только его владельцу.
    Все остальные получают запрещающий ответ.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешить чтение неавторизованным (если хотите), иначе проверьте метод
        if request.method in SAFE_METHODS:
            return True
        
        # Для изменений и удаления — проверяем, что автор совпадает с пользователем
        return obj.author == request.user
