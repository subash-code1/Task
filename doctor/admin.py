from django.contrib import admin

from .models import Department, Doctor, Token

# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation")

class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "department")

class TokenAdmin(admin.ModelAdmin):
    list_display = ("number","token_name","doctor_name","current_token","approximate_waiting_time","created_at","department","doctor")

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Token, TokenAdmin)
