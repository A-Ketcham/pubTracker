from django.contrib.auth.models import TestCase
from django.test import TestCase
from django.core.urlresolvers import reverse, resolve
from forms.views import 
from django.db import DataError
from django.core.exceptions
import validators
from forms.models import User
from forms.models import Zip
from forms.models import urls.py
"""CDT Perlee, Devin '15. Assistance given written. CDT Perlee had the modelform imported 
in order to make his test cases run. The same was done in our test cases and put into models.py
as well as our views.py
"""
from forms.views import TrackerModelForm
from forms.models import Zip, UserProfile, Transportation, TravelPlan


class QuestionURLTests(TestCase):
    #See: https://docs.djangoproject.com/en/1.7/ref/urlresolvers/#resolve
    # for additional information on resolve()
    def test_url_index(self):
        """
        /models/ should resolve to models:index
        """
        resolver = resolve('/models/')
        self.assertEqual(resolver.namespace,'models')
        self.assertEqual(resolver.view_name,'models:index')
		
	def test_url_cadet(self):
        """
        /models/cadet/ should resolve to models:cadet
        """
        resolver = resolve('/models/cadet/')
        self.assertEqual(resolver.namespace,'models')
        self.assertEqual(resolver.view_name,'models:cadet')

class QuestionModelTests(TestCase):
    #max_length is enforced by django.db so we can use a simple
    #unit test for that.
	
	"""
	CDT Perlee, Devin '15. Assistance given written. CDT Perlee gave me an example of how he set
	up his max_length tests which I emulated to fit our project
	"""
    def test_question_text_max_length(self):
            zipp = Zip(zip=u'x'*10)
			form = TrackerModelForm(instance=zipp)
			self.assertFalse(form.is_valid())
		
            cityy = Zip(city=u'x'*23)
			form = TrackerModelForm(instance=cityy)
			self.assertFalse(form.is_valid())
		
            st = Zip(state=u'x'*3)
			form = TrackerModelForm(instance=st)
			self.assertFalse(form.is_valid())
			
            xnum = UserProfile(xNumber=u'x'*7)
			form = TrackerModelForm(instance=xnum)
			self.assertFalse(form.is_valid())
		
            reg = UserProfile(regiment=u'x'*2)
			form = TrackerModelForm(instance=reg)
			self.assertFalse(form.is_valid())
		
            comp = UserProfile(company=u'x'*2)
			form = TrackerModelForm(instance=comp)
			self.assertFalse(form.is_valid())
			
            fone = UserProfile(phone=u'x'*11)
			form = TrackerModelForm(instance=fone)
			self.assertFalse(form.is_valid())
		
            yr = UserProfile(year=u'x'*5)
			form = TrackerModelForm(instance=yr)
			self.assertFalse(form.is_valid())
		
            transpo = Transportation(transpoType=u'x'*11)
			form = TrackerModelForm(instance=transpo)
			self.assertFalse(form.is_valid())
			
			
class ValidatorTests(TestCase):
        
    def not_unauthorized_word(self):
        """Raise a ValidationError if the value is in the unauthorized word list.
        """
        value = 'chipmunk'
        with self.assertRaises(ValidationError):
            validators.not_unauthorized_word(value)
			
class QuestionResultsTests(TestCase):

    def test_detail_view_with_login(self):
        """
        The results view of a question should return the results if the user is
		logged in.
        """
        User.objects.create_superuser('peppizza', 'peppizza@pizza.hours', 'iheardpizza')
        self.client.login(username='peppizza',password='iheartpizza')
        question = create_question(question_text='Logged in', days=-1)
        response = self.client.get(reverse('models:cadet',args=(question.id,)))
        self.assertContains(response, 'Logged in',status_code=200)

    
class TestDatabaseQueries(TestCase):

userprofile.objects.raw('SELECT xnumber FROM forms_userprofile WHERE forms_company='A' AND forms_regiment='1'')
travelplan.objects.raw('SELECT * FROM forms_travelplan WHERE xnumber = 'x12345'')
travelplan.objects.raw('SELECT approved FROM forms_travelplan WHERE xnumber='x12345'')

# Create your tests here.


