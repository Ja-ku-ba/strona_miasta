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
        fields = ['name', 'local_street', 'local_addres']


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