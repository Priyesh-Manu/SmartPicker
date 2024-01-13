from django.contrib import admin
from . models import ContactMessage
# Register your models here.


class contact_message(admin.ModelAdmin):
    list_display =['email','message_date','message_replied',]
    list_editable=['message_replied',]
admin.site.register(ContactMessage,contact_message)