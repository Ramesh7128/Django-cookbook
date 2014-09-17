from django.forms import ModelForm, HiddenInput
from recipes.models import Ingredient

class IngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        widgets = {'recipe': HiddenInput()}

    def get_success_url(self):
		return reverse('recipe-detail', args=[self.kwargs['slug']])
