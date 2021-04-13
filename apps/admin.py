from apps.models import App
from django.contrib import admin

# Register your models here.


@admin.register(App)
class AdminAppModel(admin.ModelAdmin):
    list_display = ["slug", "created_at", "updated_at", "token", "people", "owner"]
    readonly_fields = ["token"]
    search_fields = ["slug"]
