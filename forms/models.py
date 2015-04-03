from django.db import models

# Create your models here.

class Users(models.Model):
	userID = models.AutoField(primary_key=True, editable=False)
	email = models.EmailField(max_length=254)
	password = models.SlugField() 
	#A SlugField is a short label for something, containing only letters, numbers, underscores or hyphens.
	case = models.CharField(max_length= 10, null=True)

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
	userID = models.ForeignKey(Users)
	
class ZIP(models.Model):
	zip = models.IntegerField(max_length=9, unique=True)
	city = models.CharField(max_length=22) #Longest US city name is Rancho Santa Margarita, California
	state = models.CharField(max_length=2)

class Transportation(models.Model):
	transpoID = models.AutoField(primary_key=True)
	departTime = models.DateTimeField()
	transpoType = models.CharField(max_length=10)

class TravelPlan(models.Model):
	travelID = models.AutoField(primary_key=True)
	xNumber = models.ForeignKey(Cadet)
	transpoID = models.ForeignKey(Transportation)
	destinationAdd = models.CharField(max_length=55)
	zip= models.ForeignKey(ZIP)