from django.contrib import admin
from .models import KafedraCategory, KafedraTeacher, KafedraLife, KafedraSince, KafedraGrant, KafedraInternational, \
    KafedraCultural, KafedraTeachersUpdate


@admin.register(KafedraTeacher)
class KafedraTeacherAdmin(admin.ModelAdmin):
    list_display = ['fish', "slug", "kafedra", "birthday", "status"]
    list_filter = ["status", "created_time", "published_time"]
    search_fields = ["fish", "birthday"]
    prepopulated_fields = {"slug": ("fish",)}
    ordering = ["status", "published_time"]
    date_hierarchy = "published_time"


@admin.register(KafedraCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(KafedraLife)
class KafedraLifeAdmin(admin.ModelAdmin):
    list_display = ['title', "slug", "kafedra", "published_time", "status"]
    list_filter = ["status", "created_time", "published_time"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["status", "published_time"]
    date_hierarchy = "published_time"


@admin.register(KafedraSince)
class KafedraSinceAdmin(admin.ModelAdmin):
    list_display = ['name', "slug", "kafedra", "published_time", "status"]
    list_filter = ["status", "created_time", "published_time"]
    search_fields = ["name", "body"]
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["status", "published_time"]
    date_hierarchy = "published_time"


@admin.register(KafedraGrant)
class KafedraGrantAdmin(admin.ModelAdmin):
    list_display = ['name', "slug", "kafedra", "published_time", "status"]
    list_filter = ["status", "created_time", "published_time"]
    search_fields = ["name", "body"]
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["status", "published_time"]
    date_hierarchy = "published_time"


@admin.register(KafedraCultural)
class KafedraCulturalAdmin(admin.ModelAdmin):
    list_display = ['title', "slug", "kafedra", "published_time", "status"]
    list_filter = ["status", "created_time", "published_time"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["status", "published_time"]
    date_hierarchy = "published_time"


@admin.register(KafedraInternational)
class KafedraInternationalAdmin(admin.ModelAdmin):
    list_display = ['name', "slug", "kafedra", "published_time", "status"]
    list_filter = ["status", "created_time", "published_time"]
    search_fields = ["name", "body", "district"]
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["status", "published_time"]
    date_hierarchy = "published_time"


@admin.register(KafedraTeachersUpdate)
class KafedraTeacherUpdateAdmin(admin.ModelAdmin):
    list_display = ['fish', "kafedra", "teacher_updated_time", "status"]
    list_filter = ["status", "created_time", "published_time"]
    search_fields = ["fish"]
    ordering = ["status", "teacher_updated_time"]
    date_hierarchy = "published_time"