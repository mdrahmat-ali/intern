from django.contrib import admin
from testapp.models import User,Artist,Work

class UserAdmin(admin.ModelAdmin):
    list_display=['name','age','city']

class ArtistAdmin(admin.ModelAdmin):
    list_display=['name','work']

class WorkAdmin(admin.ModelAdmin):
    list_display=['name','work_type']

admin.site.register(User,UserAdmin)
admin.site.register(Artist,ArtistAdmin)
admin.site.register(Work,WorkAdmin)
