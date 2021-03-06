from django.contrib import admin
from recipes.models import Food, Recipe, Ingredient

admin.site.register(Food)
admin.site.register(Recipe)


class IngredientAdmin(admin.ModelAdmin):
	list_display = ('food', 'amount', 'measurement', 'recipe')

admin.site.register(Ingredient, IngredientAdmin)