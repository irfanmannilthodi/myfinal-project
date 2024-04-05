from django.contrib import admin
from . models import Marvel,Dccomics,Monster
# Register your models here.
admin.site.register(Marvel)
admin.site.register(Dccomics)
admin.site.register(Monster)