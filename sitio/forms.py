from django import forms
from django.conf import settings
from .models import Question
import datetime


class QuestionForm(forms.Form):

	choice = forms.ChoiceField( 
		required=True, 
		#choices=SELECT,
		)

	def __init__(self, *args, **kwargs):
		super(QuestionForm, self).__init__(*args, **kwargs)
		#self.fields['text'].widget.attrs['class'] = 'form-control'
		self.fields['choice'].widget.attrs['class'] = 'form-control'

