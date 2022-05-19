from django.contrib import admin

from .models import Project, Request

# Register your models here.

class RequestAdmin(admin.ModelAdmin):
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "comment",
        "sent_time",
    )

admin.site.register(Project)
admin.site.register(Request, RequestAdmin)
