from django.contrib import admin
from .models import User


# Кастомный класс для отображения пользователей
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number")
    list_filter = ("is_staff", "is_active")


admin.site.register(User, UserAdmin)
