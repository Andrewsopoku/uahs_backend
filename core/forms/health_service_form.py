from countries_plus.models import Country
from django import forms

class NewHealthServiceForm(forms.Form):
    #logo = forms.ImageField()
    name = forms.CharField(max_length=255 ,widget=forms.TextInput(attrs={
        'class': "form-control mb-4 input-rounded",'placeholder':'Name of Health Service'}),)
    country = forms.ChoiceField(required=False,widget=forms.Select(
        attrs={'class': "form-control mb-4 input-rounded",}),)
    area_of_operation = forms.CharField(max_length=255,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Area of operation'}),)
    email = forms.EmailField(max_length=255,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Email'}),)
    mobile = forms.CharField(max_length=255,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Mobile'}),)
    has_ambulance = forms.BooleanField(required=False,widget=forms.CheckboxInput(
        attrs={'class': " custom-control-input",}))

    region = forms.CharField(max_length=255,required=False,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Region'}),)
    town = forms.CharField(max_length=255, required=False,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Town'}), )
    gps_long = forms.CharField(max_length=255, required=False,widget=forms.TextInput(attrs={'class': "form-control mb-4 input-rounded"}), )
    gps_lat = forms.CharField(max_length=255, required=False,widget=forms.TextInput(attrs={'class': "form-control mb-4 input-rounded"}), )

    contact_person_first_name = forms.CharField(max_length=255, required=False, widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Contact Person First Name'}), )
    contact_person_last_name = forms.CharField(max_length=255, required=False,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Contact Person Last Name'}), )
    contact_person_address = forms.CharField(max_length=255,required=False,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Contact Person Address'}),)
    contact_person_phone_number = forms.CharField(max_length=255,required=False,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Contact Person Phone Number'}),)
    contact_person_email = forms.CharField(max_length=255, required=False,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Contact Person Email'}), )

    def __init__(self, data=None,  initial=None, instance=None):
        super(NewHealthServiceForm, self).__init__(data=data, initial=initial, )
        countries = Country.objects.all()
        choices = [(product.iso_numeric, product.name) for product in countries]

        self.fields['country'].choices =[("", "Select Country"), ] + choices

