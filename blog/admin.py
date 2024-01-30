from django.contrib import admin
from .models import Blog, Category, Education
from django.utils.safestring import mark_safe


class fastActivate(admin.ModelAdmin):
    list_display = ["name","is_active","slug",]
    list_editable = ["is_active"]
    list_filter = ["is_active", ]

class fastForEducation (admin.ModelAdmin):
    list_display = ["name","is_active","slug","selected_categories"]
    list_editable = ["is_active"]
    list_filter = ["is_active", "categories",]

    def selected_categories (self, object):

        html = "<ul>"

        for ct in object.categories.all():
            html += "<li>" + ct.name  + "</li>"

        html += "<ul>"

        return mark_safe(html) 

admin.site.register(Blog, fastActivate)
admin.site.register(Category)
admin.site.register(Education, fastForEducation)


# Register your models here.
