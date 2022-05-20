from django.contrib import admin

from About_Us.models import Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    List_display=('id','tid','tname','temail')

admin.site.register(Teacher)
