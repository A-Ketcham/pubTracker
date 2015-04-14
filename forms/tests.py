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
    def test_question_text_max_length(self):
        """
        Should not allow question text longer than 9 integers
        """
        with self.assertRaises(DataError):
            zip = create_zip(zip=u'1'*10)
			
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

    

# Create your tests here.

