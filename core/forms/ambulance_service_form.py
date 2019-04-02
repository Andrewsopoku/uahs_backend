
from django import forms

from core.models.ambulance import Ambulance
from core.models.ambulance_driver import AmbulanceDriver


class AssignDriverAmbulance(forms.Form, ):
    def __init__(self,amb_service, data=None, initial=None, instance=None):
        super(AssignDriverAmbulance, self).__init__(data=data, initial=initial, )

        choices = map(lambda ambulance: (ambulance.id, '{}'.format(ambulance.registration_number,
                                                         )), Ambulance.objects.filter(ambulance_service=amb_service))
        self.fields['ambulance'].choices = choices

        choices = map(lambda driver: (driver.id, '{}'.format(driver.driver_license_number,
                                                                   )),
                      AmbulanceDriver.objects.filter(ambulance_service=amb_service))
        self.fields['driver'].choices = choices

    ambulance = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control mb-4 input-rounded searchable", 'searchable': "Search here.."}), )
    driver = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control mb-4 input-rounded searchable", 'searchable': "Search here.."}), )
