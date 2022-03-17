from django.contrib import admin

from .models import Student, Teacher, Relation


class RelationInline(admin.TabularInline):
    model = Relation
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    list_filter = ['group']
    inlines = [
        RelationInline,
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    inlines = [
        RelationInline,
    ]
