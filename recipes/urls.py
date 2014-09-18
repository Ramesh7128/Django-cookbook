from django.conf.urls import patterns, include, url
from recipes.views import FoodListView, FoodDetailView, FoodCreateView, FoodDeleteView, RecipeListView, RecipeCreateView, RecipeDetailView, RecipeUpdateView, RecipeDeleteView, IngredientCreateView, IngredientDeleteView 


urlpatterns = patterns('',
	url(r'^food/$', FoodListView.as_view(), name='food-list'),
	url(r'^food/(?P<pk>\d+)$', FoodDetailView.as_view(), name='food-detail'),
	url(r'^food/create$', FoodCreateView.as_view(), name = 'food-create'),
	url(r'^food/(?P<pk>\d+)/remove_food$', FoodDeleteView.as_view(), name ='food-delete'),
	url(r'^$', RecipeListView.as_view(), name='recipe-list'),
	url(r'^new/$', RecipeCreateView.as_view(), name='recipe-create'),
	url(r'^(?P<slug>[-\w]+)$', RecipeDetailView.as_view(), name='recipe-detail'),
	url(r'^(?P<slug>[-\w]+)/update$', RecipeUpdateView.as_view(), name='recipe-update'),
	url(r'^(?P<slug>[-\w]+)/remove_recipe$', RecipeDeleteView.as_view(), name='recipe-delete'),
	url(r'^(?P<slug>[-\w]+)/add_ingredient/$', IngredientCreateView.as_view(), name='ingredient-create'),
	url(r'^(?P<slug>[-\w]+)/remove_ingredient/(?P<pk>\d+)/$', IngredientDeleteView.as_view(), name='ingredient-delete'),
	





        )