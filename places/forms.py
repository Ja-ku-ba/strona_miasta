from .models import Locals, LocalProducts, LocalRating
from django.forms import ModelForm

class LocalsForm(ModelForm):
    class Meta():
        model = Locals
        fields = '__all__'


class LocalProductsForm(ModelForm):
    class Meta():
        model = LocalProducts
        fields = '__all__'


class LocalRatingForm(ModelForm):
    class Meta():
        model = LocalRating
        fields = '__all__'