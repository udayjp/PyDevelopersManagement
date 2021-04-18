from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Technology)
admin.site.register(Domain)
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(QA)
admin.site.register(Developer)
admin.site.register(Weightage)