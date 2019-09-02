
from django import forms

from core.models.ambulance import Ambulance
from core.models.ambulance_driver import AmbulanceDriver


class AssignDriverAmbulance(forms.Form, ):
    def __init__(self,amb_service, data=None, initial=None, instance=None):
        super(AssignDriverAmbulance, self).__init__(data=data, initial=initial, )

        choices = map(lambda ambulance: (ambulance.id, '{}'.format(ambulance.registration_number,
                                                         )), Ambulance.objects.filter(ambulance_service=amb_service))
        self.fields['ambulance'].choices = choices

        choices = map(lambda driver: (driver.id, '{} {}'.format(driver.user.first_name,
                                                                driver.user.surname)),
                      AmbulanceDriver.objects.filter(ambulance_service=amb_service))
        self.fields['driver'].choices = choices

    ambulance = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control mb-4 input-rounded searchable", 'searchable': "Search here.."}), )
    driver = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control mb-4 input-rounded searchable", 'searchable': "Search here.."}), )


Cities = (("Accra", "Accra"), ("Kumasi", "Kumasi"),)
Unit = (("Metre", "Metre"), ("Kilometre", "Kilometre"),)


class SetAmbulanceServicePrice(forms.Form, ):

    city = forms.ChoiceField(choices=Cities,widget=forms.Select(attrs={'class': "form-control mb-4 input-rounded searchable", 'searchable': "Search here.."}), )
    distance_unit = forms.ChoiceField(choices=Unit,widget=forms.Select(attrs={'class': "form-control mb-4 input-rounded searchable", 'searchable': "Search here.."}), )

    minumum_rate = forms.CharField(max_length=255, widget=forms.NumberInput(attrs={
        'class': "form-control mb-4 input-rounded", 'placeholder': 'Minimum rate'}), )

    minumum_distance = forms.CharField(max_length=255, widget=forms.NumberInput(attrs={
        'class': "form-control mb-4 input-rounded", 'placeholder': 'Minimum distance'}), )

    rate_per_minumum_distance = forms.CharField(max_length=255, widget=forms.NumberInput(attrs={
        'class': "form-control mb-4 input-rounded", 'placeholder': 'Rate per distance'}), )
