from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import (ExportForm, ImportForm,
                                                SelectableFieldsExportForm)
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
admin.site.site_header = _("CRM Admin")
admin.site.site_title = _("CRM Admin Portal")
admin.site.index_title = _("Welcome to CRM Admin Portal!")




from django.utils.html import format_html


@admin.register(Membership )
class MembershipAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('id',  'created_at', 'updated_at', 'name', 'colored_plan', 'membership_active', 'unique_code' )
    list_filter = ('membership_plan', 'membership_active', 'created_at', 'updated_at')
    search_fields = ('name', 'unique_code')
    ordering = ('id', 'name')
    # readonly_fields = ('unique_code',)
    list_per_page = 20
    list_display_links = ('id', 'name', 'colored_plan')
    list_editable = ('membership_active', 'unique_code',)
    date_hierarchy = 'created_at'  # Enables date-based drilldown navigation
    actions = ['unique_code']
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm

    def colored_plan(self, obj):
        color = {
            'S': 'blue',
            'P': 'green',
            'UX': 'purple',
        }.get(obj.membership_plan, 'black')

        label = dict(obj.MEMBERSHIP_CHOICES).get(obj.membership_plan, obj.membership_plan)
        return format_html('<span style="color: {};">{}</span>', color, label)

    colored_plan.short_description = _('Membership Plan')
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
