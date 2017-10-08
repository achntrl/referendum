from django.contrib import admin

from .models import User, UserProfile


class UserProfileAdmin(admin.StackedInline):
    model = UserProfile
    can_delete = False
    list_display = ('first_name', 'last_name')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'profile_first_name', 'profile_last_name')
    inlines = (UserProfileAdmin, )

    def profile_first_name(self, instance):
        return instance.profile.first_name

    def profile_last_name(self, instance):
        return instance.profile.last_name


admin.site.register(User, UserAdmin)
