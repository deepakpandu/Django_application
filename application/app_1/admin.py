from django.contrib import admin
from django.contrib import admin
from app_1.models import tech


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "phone","address",)
admin.site.register(tech, MemberAdmin)

# Register your models here.

