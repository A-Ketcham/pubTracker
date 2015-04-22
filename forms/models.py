from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	FIRST = '1'
	SECOND = '2'
	THIRD = '3'
	FOURTH = '4'
	REG_CHOICES = (
		(FIRST, '1'),
		(SECOND, '2'),
		(THIRD, '3'),
		(FOURTH, '4'),
	)
	
	ALPHA = 'A'
	BRAVO = 'B'
	CHARLIE = 'C'
	DELTA = 'D'
	ECHO = 'E'
	FOXTROT = 'F'
	GOLF = 'G'
	HOTEL = 'H'
	INDIA = 'I'
	CO_CHOICES = (
		(ALPHA, 'A'),
		(BRAVO, 'B'),
		(CHARLIE, 'C'),
		(DELTA, 'D'),
		(ECHO, 'E'),
		(FOXTROT, 'F'),
		(GOLF, 'G'),
		(HOTEL, 'H'),
		(INDIA, 'I'),
	)
	
	user = models.OneToOneField(User)
	xNumber = models.CharField(max_length=6, unique=True, blank=True, default='x00000')
	regiment = models.CharField(max_length=1, choices=REG_CHOICES, blank=True, default= FIRST)
	company = models.CharField(max_length=1, choices=CO_CHOICES, blank=True, default= ALPHA)
	year = models.IntegerField(max_length=4, blank=True, default='0000')
	phone = models.IntegerField(max_length=10, blank=True, default='1112223334')
	
	def __str__(self):
		return self.user.username
	
class ZIP(models.Model):
	zip = models.IntegerField(max_length=9)
	city = models.CharField(max_length=22)
	state = models.CharField(max_length=2)
	
	def __str__(self):              # __unicode__ on Python 2
		return str(self.zip)

class Transportation(models.Model):
	PLANE= 'A'
	TRAIN= 'B'
	POV= 'C'
	NONPOV= 'D'
	CASE_CHOICES = (
		(PLANE, 'Plane'),
		(TRAIN, 'Train'),
		(POV, 'POV'),
		(NONPOV, 'Non-POV'),
	)
	transpoID = models.AutoField(primary_key=True)
	departTime = models.DateTimeField()
	transpoType = models.CharField(max_length=10, choices=CASE_CHOICES)
	
	def __str__(self):              # __unicode__ on Python 2
		return str(self.transpoID)

class Plane(Transportation):
	flightID = models.CharField(max_length=10)
	flightDate = models.DateTimeField()
	airportCode = models.CharField(max_length=3)
	
class Train(Transportation):
	station = models.CharField(max_length=25)

class POV(Transportation):
	licenseNum = models.CharField(max_length=10)
	make = models.CharField(max_length=25)
	model = models.CharField(max_length=25)

class NonPOV(Transportation):
	type = models.CharField(max_length=25)

class TravelPlan(models.Model):
	LOCATOR_YES_NO_CHOICES = ( (True,'Yes'), (False, 'No'))
	travelID = models.AutoField(primary_key=True)
	xNumber = models.ForeignKey(UserProfile)
	transpoID = models.ForeignKey(Transportation)
	destinationAdd = models.CharField(max_length=55)
	zip= models.ForeignKey(ZIP, blank=True, default='000010000')
	editDate = models.DateTimeField(null=True)
	approved = models.NullBooleanField(choices=LOCATOR_YES_NO_CHOICES,
                                max_length=3,
                                blank=True, default=False,)
	
	def __str__(self):              # __unicode__ on Python 2
		return str(self.travelID)
	def edited_recently(self):
		return self.editDate >= timezone.now() - datetime.timedelta(days=1)