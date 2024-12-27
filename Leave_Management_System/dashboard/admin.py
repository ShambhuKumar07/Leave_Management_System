from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import ProfileDetails

@admin.register(ProfileDetails)
class ProfileDetailsAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'email', 'mobile', 'gender', 'dob')
    search_fields = ('code', 'name', 'email')
