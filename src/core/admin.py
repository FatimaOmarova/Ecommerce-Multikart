from django.contrib import admin

# Register your models here.
from core import models

# cavid1
# cavid1234

class StaffModelAdmin(admin.ModelAdmin):
    list_display = ("full_name",)
    search_fields = ['full_name']


class FaqModelAdmin(admin.ModelAdmin):
    list_display = ("title",)


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ("first_name",)



class SubscribeModelAdmin(admin.ModelAdmin):
    list_display = ("email",)



class InstagramModelAdmin(admin.ModelAdmin):
    list_display = ("image",)


class LogosModelAdmin(admin.ModelAdmin):
    list_display = ("image",)


class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ("full_name",)


class BlogsModelAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(models.Staff, StaffModelAdmin)
admin.site.register(models.Faq, FaqModelAdmin)
admin.site.register(models.Contact, ContactModelAdmin)
admin.site.register(models.Subscribers, SubscribeModelAdmin)
admin.site.register(models.Instagram, InstagramModelAdmin)
admin.site.register(models.Logo, LogosModelAdmin)
admin.site.register(models.Comment, CommentsModelAdmin)
admin.site.register(models.Blog, BlogsModelAdmin)

