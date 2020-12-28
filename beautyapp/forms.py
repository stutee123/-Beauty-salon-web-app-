from .models import *
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class BookingHairCareForm(forms.ModelForm):
    haircare=forms.ModelChoiceField(queryset=HairCare.objects, empty_label=None)
    class Meta:
        model = BookingHaircare
        fields = '__all__'

class BookingMakeUpServicesForm(forms.ModelForm):
    makeupservices=forms.ModelChoiceField(queryset=MakeUpServices.objects, empty_label=None)
    class Meta:
        model = BookingMakeUpServices
        fields = '__all__'

class BookingFacialTreatmentForm(forms.ModelForm):
    facialtreatment=forms.ModelChoiceField(queryset=FacialTreatment.objects, empty_label=None)
    class Meta:
        model = BookingFacialTreatment
        fields = '__all__'

class BookingNailArtsForm(forms.ModelForm):
    nailarts=forms.ModelChoiceField(queryset=NailArts.objects, empty_label=None)
    class Meta:
        model = BookingNailArts
        fields = '__all__'

class BookingHairStylesForm(forms.ModelForm):
    hairstyles=forms.ModelChoiceField(queryset=HairStyles.objects, empty_label=None)
    class Meta:
        model = BookingHairStyles
        fields = '__all__'

class BookingPedicureForm(forms.ModelForm):
    pedicure=forms.ModelChoiceField(queryset=Pedicure.objects, empty_label=None)
    class Meta:
        model = BookingPedicure
        fields = '__all__'

class BookingManicureForm(forms.ModelForm):
    manicure=forms.ModelChoiceField(queryset=Manicure.objects, empty_label=None)
    class Meta:
        model = BookingManicure
        fields = '__all__'