from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from unfold.admin import ModelAdmin
from unfold.forms import (AdminPasswordChangeForm, UserChangeForm,
                          UserCreationForm)

from .models import Membership

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


# admin.site.register(Membership)
# admin.site.unregister(User) # Unregister the User model to prevent it from being displayed in the admin interface
# admin.site.unregister(Group) # Unregister the Group model to prevent it from being displayed in the admin interface

# Costumization admin title and header
admin.site.site_header = "CRM Admin"
admin.site.site_title = "CRM Admin Portal"
admin.site.index_title = "Welcome to CRM Admin Portal!"


### Admin configuration for the Membership model
# @admin.register(Membership)
# class MembershipAdmin(admin.ModelAdmin):
#     """
#     Administrator configuration for the Membership model.

#     This class defines the display and behavior of the Membership model
#     in the Django admin interface. Currently configured with default settings.

#     Attributes:
#         None specified yet - using default ModelAdmin configuration.

#     Methods:
#         None specified yet - using default ModelAdmin behavior.
#     """
#     pass

# #admin.site.register(Membership, MembershipAdmin)

# Keep all of variables which we are adding manually
# @admin.register(Membership)
# class MembershipAdmin(admin.ModelAdmin):
#     """
#     Admin configuration for the Membership model.

#     This class configures how the Membership model is displayed and managed in the Django admin interface.

#     Parameters
#     ----------
#     admin : django.contrib.admin
#         The Django admin module.

#     Attributes
#     ----------
#     list_display : tuple
#         Fields to display in the list view ('name', 'membership_plan', 'membership_active', 'unique_code').
#     search_fields : tuple
#         Fields that can be searched in the admin ('name', 'unique_code').
#     list_filter : tuple
#         Fields that can be used to filter the list view ('membership_plan', 'membership_active').
#     """
#     list_display = ('name', 'membership_plan', 'membership_active', 'unique_code')
#     search_fields = ('name', 'unique_code')
#     list_filter = ('membership_plan', 'membership_active' , 'unique_code')


#  # Keep all of variables except one of them
# @admin.register(Membership)
# class MembershipAdmin(admin.ModelAdmin):
#     exclude = ('unique_code',)  # Exclude the unique_code field from the admin form
#     list_display = ('name', 'membership_plan', 'membership_active')
#     search_fields = ('name' , )
#     list_filter = ('membership_plan', 'membership_active')





# Read only and no one can remove users
# @admin.register(Membership)
# class MembershipAdmin(admin.ModelAdmin):
#     """
#     Admin configuration for the Membership model.

#     This class configures how the Membership model is displayed and managed in the Django admin interface.

#     Attributes
#     ----------
#     list_display : tuple
#         Fields to display in the list view.
#     search_fields : tuple
#         Fields that can be searched in the admin.
#     list_filter : tuple
#         Fields that can be used to filter the list view.
#     """

#     list_display = ('name', 'membership_plan', 'membership_active', 'unique_code')
#     search_fields = ('name', 'unique_code')
#     list_filter = ('membership_plan', 'membership_active', 'unique_code')
#     list_editable = ('membership_plan', 'membership_active', 'unique_code',)

#     def has_delete_permission(self, request, obj=None):
#         """Disables delete permission for all users in the admin."""
#         return False

# @admin.register(Membership)
# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'membership_plan', 'membership_active', 'unique_code')
#     list_filter = ('membership_plan', 'membership_active')
#     search_fields = ('name', 'unique_code')
#     ordering = ('id', 'name')
#     readonly_fields = ('unique_code',)
#     list_per_page = 20
#     list_display_links = ('id', 'name', 'membership_plan')  # Make these fields clickable
#     # list_editable = ('membership_plan', 'membership_active', 'unique_code',)


#     def has_delete_permission(self, request, obj=None):
#         # Allow delete option in admin
#         return True

from django.utils.html import format_html


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id',  'created_at', 'updated_at', 'name', 'colored_plan', 'membership_active', 'unique_code' )
    list_filter = ('membership_plan', 'membership_active', 'unique_code', 'created_at', 'updated_at')
    search_fields = ('name', 'unique_code')
    ordering = ('id', 'name')
    # readonly_fields = ('unique_code',)
    list_per_page = 20
    list_display_links = ('id', 'name', 'colored_plan')
    list_editable = ('membership_active', 'unique_code',)
    date_hierarchy = 'created_at'  # Enables date-based drilldown navigation

    def colored_plan(self, obj):
        color = {
            'S': 'blue',
            'P': 'green',
            'UX': 'purple',
        }.get(obj.membership_plan, 'black')

        label = dict(obj.MEMBERSHIP_CHOICES).get(obj.membership_plan, obj.membership_plan)
        return format_html('<span style="color: {};">{}</span>', color, label)

    colored_plan.short_description = 'Membership Plan'
    colored_plan.admin_order_field = 'membership_plan'  # optional: allow sorting

    # # Allow delete option in admin
    def has_delete_permission(self, request, obj=None):
        if obj != None and request.POST.get('action') == 'delete_selected':
            # Message to prevent deletion
            self.message_user(request, "Deletion is not allowed for Membership records.", level='error')
        return True

        # add to change or not change the user
    def has_change_permission(self, request, obj=None):
        """Allow change permission for all users in the admin."""
        return False

    def has_add_permission(self, request):
        """Allow add permission for all users in the admin."""
        return False

# Register the Membership model with the custom admin class
# admin.site.register(Membership, MembershipAdmin)
