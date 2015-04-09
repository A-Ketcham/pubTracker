from django.contrib import admin

# Register your models here.

from .models import Cadet, Transportation, ZIP, TravelPlan, Train, Plane, POV, NonPOV

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
	fields = ('xNumber', ('firstName', 'lastName'), ('company', 'regiment'), 'year', 'phone', 'email')
	list_display = ('xNumber', 'lastName', 'company', 'regiment')
	#readonly_fields = ('xNumber', 'email')

class TravelPlanAdmin(admin.ModelAdmin):
	list_display = ('xNumber', 'transpoID', 'editDate')
	
admin.site.register(Cadet, CadetAdmin)
admin.site.register(Transportation, TranspoAdmin)
admin.site.register(ZIP)
admin.site.register(TravelPlan, TravelPlanAdmin)