from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("rating", "author")
    list_display = ("title", "author")


admin.site.register(Book, BookAdmin)
