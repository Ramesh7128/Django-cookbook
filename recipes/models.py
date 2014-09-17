from django.db import models

# Create your models here.

MEASUREMENT_CHOICES = ((1,"piece"),(2,"liter"),(3,"cup"),(4,'tablespoon'),(5,"teaspoon"))

class Food(models.Model):
	name = models.CharField(max_length=20, unique=True)
	def __unicode__(self):
		return self.name
	@models.permalink
	def get_absolute_url(self):
		return ('food-detail', [self.id])

class Recipe(models.Model):
	title = models.CharField(max_length=80, unique=True)
	slug = models.SlugField(max_length=80, unique=True)
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.title
	
	@models.permalink
	def get_absolute_url(self):
		return ('recipe-detail', [self.slug])

class Ingredient(models.Model):
	recipe = models.ForeignKey(Recipe)
	food = models.ForeignKey(Food)
	amount = models.DecimalField(decimal_places=2, max_digits=4)
	measurement = models.SmallIntegerField(choices= MEASUREMENT_CHOICES)

	def __unicode__(self):
		return "%0.2g %s %s (%s)" % (self.amount, self.get_measurement_display(), self.food, self.recipe)

