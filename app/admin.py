from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):  # или StackedInline
    model = ProjectImage
    extra = 1  # сколько пустых форм показывать
    fields = ['image', 'order']
    show_change_link = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ProjectImageInline]


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'image', 'order']
    list_filter = ['project']