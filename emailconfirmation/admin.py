from django.contrib import admin

from emailconfirmation.models import EmailAddress, EmailConfirmation

class EmailConfirmationAdmin(admin.ModelAdmin):

        raw_id_fields = ('email_address',)


admin.site.register(EmailAddress)
admin.site.register(EmailConfirmation, EmailConfirmationAdmin)
