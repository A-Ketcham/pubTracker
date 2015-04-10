from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	
	def __str__(self):
		return self.user.username

class Cadet(models.Model):
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
	
	xNumber = models.IntegerField(max_length=5, unique=True, primary_key=True)
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=25)
	regiment = models.CharField(max_length=1, choices=REG_CHOICES, default= FIRST)
	company = models.CharField(max_length=1, choices=CO_CHOICES, default= ALPHA)
	year = models.IntegerField(max_length=4)
	phone = models.IntegerField(max_length=10)
	email = models.ForeignKey(UserProfile)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.firstName+" "+self.lastName
		
class ZIP(models.Model):
	zip = models.IntegerField(max_length=9, unique=True)
	city = models.CharField(max_length=22) #Longest US city name is Rancho Santa Margarita, California
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
	travelID = models.AutoField(primary_key=True)
	xNumber = models.ForeignKey(Cadet)
	transpoID = models.ForeignKey(Transportation)
	destinationAdd = models.CharField(max_length=55)
	zip= models.ForeignKey(ZIP)
	editDate = models.DateTimeField(null=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return str(self.travelID)
	def edited_recently(self):
		return self.editDate >= timezone.now() - datetime.timedelta(days=1)