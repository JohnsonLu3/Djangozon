from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(items)
admin.site.register(tag)
admin.site.register(hadTag)
admin.site.register(seller)
admin.site.register(users)