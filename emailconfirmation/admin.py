from django.contrib import admin

from emailconfirmation.models import EmailAddress, EmailConfirmation


class EmailAddressAdmin(admin.ModelAdmin):

        raw_id_fields = ('user',)


class EmailConfirmationAdmin(admin.ModelAdmin):

        search_fields = ('email_address__email', 'email_address__user__username', 'email_address__user__id',)
        raw_id_fields = ('email_address',)


admin.site.register(EmailAddress, EmailAddressAdmin)
admin.site.register(EmailConfirmation, EmailConfirmationAdmin)
