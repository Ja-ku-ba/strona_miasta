from .models import District, Street, Locals, LocalStaff, LocalProducts, LocalRating
from django.forms import ModelForm

class DistrictForm(ModelForm):
    class Meta():
        model = District
        fields = '__all__'


class StreetForm(ModelForm):
    class Meta():
        model = Street
        fields = '__all__'


class LocalsForm(ModelForm):
    class Meta():
        model = Locals
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(LocalsForm, self).__init__(*args, **kwargs)
        self.fields['local_street'].required = False
        self.fields['local_addres'].required = False
        self.fields['name'].required = False
        self.fields['description'].required = False


class LocalStaffForm(ModelForm):
    class Meta():
        model = LocalStaff
        fields = '__all__'


class LocalProductsForm(ModelForm):
    class Meta():
        model = LocalProducts
        fields = '__all__'


class LocalRatingForm(ModelForm):
    class Meta():
        model = LocalRating
        fields = '__all__'