from django.contrib import admin

# Register your models here.

from .models import Users, Cadet, Transportation, ZIP, TravelPlan, Train, Plane, POV, NonPOV

admin.site.register(Users)
admin.site.register(Cadet)
admin.site.register(Transportation)
admin.site.register(ZIP)
admin.site.register(TravelPlan)
admin.site.register(Train)
admin.site.register(Plane)
admin.site.register(POV)
admin.site.register(NonPOV)