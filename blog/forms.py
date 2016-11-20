from django import forms
from .models import Guest
from django.utils.translation import ugettext_lazy as _



class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, required=True)
    conjoint = forms.CharField(max_length=100, required=False)
    adresse = forms.CharField(max_length=100,required=True)
    enfants = forms.BooleanField(help_text="Viendrez-vous avec vos enfants?", required=False)




class GuestForm(forms.ModelForm):
	class Meta:
		model = Guest
		fields = ['nom', 'conjoint','enfants','adresse']
		labels = {
            'nom':_('Je suis (*)' ), 
            'conjoint': _('Je viendrai avec:'),
            'enfants':_('et nos enfants'),
            'adresse':_('Notre adresse est (*) '),
            

        }