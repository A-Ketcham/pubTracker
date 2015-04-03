from django.contrib import admin

# Register your models here.

from .models import Users, Cadet, Transportation, ZIP, TravelPlan

admin.site.register(Users)
admin.site.register(Cadet)
admin.site.register(Transportation)
admin.site.register(ZIP)
admin.site.register(TravelPlan)