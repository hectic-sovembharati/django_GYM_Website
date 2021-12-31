from django.contrib import admin

from home.models import About, Home, Members


# Register your models here.
admin.site.register(About)
admin.site.register(Members)

admin.site.register(Home)