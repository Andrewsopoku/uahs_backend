
from django import forms

from countries_plus.models import Country


class NewAmbulanceServiceForm(forms.Form):
    #logo = forms.ImageField()
    name = forms.CharField(max_length=255 ,widget=forms.TextInput(attrs={
        'class': "form-control mb-4 input-rounded",'placeholder':'Name of Ambulance Service'}),)
    country = forms.ChoiceField(required=False,widget=forms.Select(
        attrs={'class': "form-control mb-4 input-rounded",}),)
    area_of_operation = forms.CharField(max_length=255,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Area of operation'}),)
    email = forms.EmailField(max_length=255,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Email'}),)
    mobile = forms.CharField(max_length=255,widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Mobile'}),)

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
        super(NewAmbulanceServiceForm, self).__init__(data=data, initial=initial, )
        countries = Country.objects.all()
        choices = [(product.iso_numeric, product.name) for product in countries]

        self.fields['country'].choices =[("", "Select Country"), ] + choices



Title = (("Mr", "Mr"), ("Mrs", "Mrs"),("Dr", "Dr"),("Miss","Miss"),("Ms","Ms"),("Prof","Prof"),("Pr","Pr"),("Rev.","Rev."),
        ("Nana","Nana"))
Sex = (("Male", "Male"), ("Female", "Female"))
Marital_status = (("Single","Single"),("Married","Married"))

class NewAmbulanceServiceAdminForm(forms.Form):

        #picture = forms.ImageField()
        first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
            'class': "form-control mb-4 input-rounded",'placeholder':'First Name'}), )

        surname = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control mb-4 input-rounded",
                                                                                'placeholder':'Surname'}), )
        sex = forms.ChoiceField(choices=Sex, widget=forms.RadioSelect(attrs={'class': "", }),
                                required=False)

        date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker form-control mb-4 input-rounded','placeholder':'Date of Birth','type':"date"}),
                                        input_formats=["%Y-%m-%d"])
        nationality = forms.ChoiceField(required=False,widget=forms.Select(attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Nationality'}), )

        address = forms.CharField(max_length=255, required=False,
                                  widget=forms.TextInput(attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Address'}), )

        email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Email'}), )
        mobile = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control mb-4 input-rounded",'placeholder':'Phone Number'}), )

        def __init__(self, data=None,  initial=None, instance=None):
                super(NewAmbulanceServiceAdminForm, self).__init__(data=data, initial=initial, )
                countries = Country.objects.all()
                choices = [(product.iso_numeric, product.name) for product in countries]

                self.fields['nationality'].choices =[("", "Select Country"), ] + choices


class NewAmbulanceDriverForm(forms.Form):
    # picture = forms.ImageField()
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': "form-control mb-4 input-rounded", 'placeholder': 'First Name'}), )

    surname = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control mb-4 input-rounded",
                                                                            'placeholder': 'Surname'}), )
    sex = forms.ChoiceField(choices=Sex, widget=forms.RadioSelect(attrs={'class': "", }),
                            required=False)

    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'datepicker form-control mb-4 input-rounded', 'placeholder': 'Date of Birth', 'type': "date"}),
                                    input_formats=["%Y-%m-%d"])
    nationality = forms.ChoiceField(required=False, widget=forms.Select(
        attrs={'class': "form-control mb-4 input-rounded", 'placeholder': 'Nationality'}), )

    address = forms.CharField(max_length=255, required=False,
                              widget=forms.TextInput(
                                  attrs={'class': "form-control mb-4 input-rounded", 'placeholder': 'Address'}), )

    email = forms.EmailField(max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded", 'placeholder': 'Email'}), )
    mobile = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded", 'placeholder': 'Phone Number'}), )
    driver_license_number = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control mb-4 input-rounded", 'placeholder': 'Drivers License Number' }), )

    def __init__(self, data=None, initial=None, instance=None):
        super(NewAmbulanceDriverForm, self).__init__(data=data, initial=initial, )
        countries = Country.objects.all()
        choices = [(product.iso_numeric, product.name) for product in countries]

        self.fields['nationality'].choices = [("", "Select Country"), ] + choices

