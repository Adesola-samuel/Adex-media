from django.contrib import admin
from .models import WorkCategory, FeaturedWork, Message

admin.site.register(Message)
admin.site.register(WorkCategory)
admin.site.register(FeaturedWork)


