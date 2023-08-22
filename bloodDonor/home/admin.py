from django.contrib import admin
from .models import UserProfile, Contact, DonorStory

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Contact)
admin.site.register(DonorStory)
