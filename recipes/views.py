from recipes.models import Food, Recipe, Ingredient
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.forms import ModelForm, HiddenInput 

class FoodListView(ListView):
    model = Food

class FoodDetailView(DetailView):
	model = Food

class FoodCreateView(CreateView):
	model = Food

class FoodDeleteView(DeleteView):
	model = Food

	def get_success_url(self):
		return reverse('food-list', args=())


class RecipeListView(ListView):
	model = Recipe

class RecipeCreateView(CreateView):
	model = Recipe

class RecipeDetailView(DetailView):
	model = Recipe

class RecipeUpdateView(UpdateView):
	model = Recipe
	template_name = 'recipes/recipe_update_form.html'

class RecipeDeleteView(DeleteView):
	model = Recipe

	def get_success_url(self):
		return reverse('recipe-list', args=())

class IngredientCreateView(CreateView):
	model = Ingredient

	def get_initial(self, *args, **kwargs):
		recipe = Recipe.objects.get(slug=self.kwargs['slug'])
		return {'recipe': recipe}
	def get_success_url(self):
		return reverse('recipe-detail', args=[self.kwargs['slug']])

class IngredientDeleteView(DeleteView):
	model = Ingredient

	def get_success_url(self):
		return reverse('recipe-detail', args=[self.kwargs['slug']])














