from django.contrib import admin

# Register your models here.
from finance.models import Currency

class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', 'created_date', 'modified_by', 'modified_date', )

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified_by = request.user.username
        else:
            obj.created_by = request.user.username
            obj.modified_by = request.user.username
        obj.save()


@admin.register(Currency)
class CurrencyAdmin(BaseAdmin):
    list_display = ('full_name', 'name',)
