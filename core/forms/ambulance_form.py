
from django import forms

from core.models.ambulance import amb_type


class NewAmbulanceForm(forms.Form):
    registration_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': "form-control mb-4 input-rounded" ,'placeholder' :'Registration Number'}), )

    dominant_color = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control mb-4 input-rounded",
                                                                            'placeholder' :'Color'}), )
    car_model = forms.CharField(max_length=255, required=False,
                                widget=forms.TextInput
                                (attrs={'class': "form-control mb-4 input-rounded", 'placeholder': 'Make'}), )

    make_year = forms.CharField(max_length=255, required=False,
                              widget=forms.TextInput
                                  (attrs={'class': "form-control mb-4 input-rounded" ,'placeholder' :'Make Year'}), )
    type = forms.ChoiceField(choices=amb_type,widget=forms.Select(
        attrs={'class': "form-control mb-4 input-rounded searchable", 'searchable': "Search here.."}), )

