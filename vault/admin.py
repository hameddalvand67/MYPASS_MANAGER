from django.contrib import admin
from .models import Entry, Section


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1
    fields = ("label", "url", "username", "password", "extra", "order")


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "sections_count", "updated_at")
    list_filter = ("category",)
    search_fields = (
        "title", "category", "notes",
        "sections__label", "sections__url", "sections__username", "sections__extra",
    )
    inlines = [SectionInline]

    @admin.display(description="تعداد بخش‌ها")
    def sections_count(self, obj):
        return obj.sections.count()
