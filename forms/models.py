from django.db import models

# Create your models here.

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
	email = models.EmailField(max_length=254, unique=True, default='ash.ketchum@pokemon.com')
	
	def __str__(self):              # __unicode__ on Python 2
		return self.firstName+" "+self.lastName

class Users(models.Model):
	ADMIN= 'A'
	TAC= 'T'
	S1= 'S'
	CASE_CHOICES = (
		(ADMIN, 'Admin'),
		(TAC, 'TAC'),
		(S1, 'Cadet S1'),
	)

	userID = models.AutoField(primary_key=True, editable=False)
	email = models.ForeignKey(Cadet)
	password = models.SlugField() 
	#A SlugField is a short label for something, containing only letters, numbers, underscores or hyphens.
	case = models.CharField(max_length= 10, choices=CASE_CHOICES, null=True)
	
	def __str__(self):
		return self.userID
		
class ZIP(models.Model):
	zip = models.IntegerField(max_length=9, unique=True)
	city = models.CharField(max_length=22) #Longest US city name is Rancho Santa Margarita, California
	state = models.CharField(max_length=2)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.zip

class Transportation(models.Model):
	transpoID = models.AutoField(primary_key=True)
	departTime = models.DateTimeField()
	transpoType = models.CharField(max_length=10)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.transpoID

class TravelPlan(models.Model):
	travelID = models.AutoField(primary_key=True)
	xNumber = models.ForeignKey(Cadet)
	transpoID = models.ForeignKey(Transportation)
	destinationAdd = models.CharField(max_length=55)
	zip= models.ForeignKey(ZIP)
	editDate = models.DateTimeField(null=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.travelID
	def edited_recently(self):
		return self.editDate >= timezone.now() - datetime.timedelta(days=1)