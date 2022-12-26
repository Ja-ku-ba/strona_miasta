from .models import District, Street, Locals, LocalProducts
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

class LocalProductsForm(ModelForm):
    class Meta():
        model = LocalProducts
        fields = '__all__'