from django.contrib import admin
from .models import UserProfile, Cadet, Transportation, ZIP, TravelPlan, Train, Plane, POV, NonPOV


class TrainInLine(admin.StackedInline):
	model = Train
	fieldsets = [
		(Train,		{'fields': ['station'], 
					 'classes': ['collapse'],
					}),
	]

class PlaneInLine(admin.StackedInline):
	model = Plane
	fieldsets = [
		(Plane,		{'fields': ['flightID', 'flightDate', 'airportCode'], 
					 'classes': ['collapse'], 
					 'description': ('Please enter your flight number, flight departure time, and 3 letter airport code.'),
					}),
	]

class POVInLine(admin.StackedInline):
	model = POV
	fieldsets = [
		(POV,		{'fields': ['licenseNum', 'make', 'model'], 
					 'classes': ['collapse'], 
					 'description': ('Please enter the make and model of your car and your license plate number.'),
					}),
	]

class NonPOVInLine(admin.StackedInline):
	model = NonPOV
	fieldsets = [
		(NonPOV,		{'fields': ['type'], 
						 'classes': ['collapse'], 
					 'description': ('Please describe the type of transportation you are using (taxi, carpool, etc).'),
						}),
	]
	
class TranspoAdmin(admin.ModelAdmin):
	inlines = [TrainInLine, PlaneInLine, POVInLine, NonPOVInLine]
	list_display = ('transpoID', 'departTime', 'transpoType')

class CadetAdmin(admin.ModelAdmin):
	fields = ('xNumber', 'year', 'phone', 'email')
	#readonly_fields = ('xNumber', 'email')

class TravelPlanAdmin(admin.ModelAdmin):
	fields = ('xNumber', 'transpoID', 'editDate', 'destinationAdd', 'zip', 'approved')
	raw_id_fields = ('zip',)
	list_display = ('xNumber', 'transpoID', 'editDate', 'approved')

class UserProfileAdmin(admin.ModelAdmin):
	fields = ('user', ('regiment', 'company'))

class ZIPAdmin(admin.ModelAdmin):
	list_display = ('zip', 'city', 'state')
	readonly_fields = ('zip', 'city', 'state')	
		
		
admin.site.register(UserProfile, UserProfileAdmin)	
admin.site.register(Cadet, CadetAdmin)
admin.site.register(Transportation, TranspoAdmin)
admin.site.register(ZIP, ZIPAdmin)
admin.site.register(TravelPlan, TravelPlanAdmin)