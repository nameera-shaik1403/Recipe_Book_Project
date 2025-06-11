from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField(help_text='Enter one ingredients per line')
    instructions = models.TextField(help_text='Enter instructions step by step')
    preparation_time = models.IntegerField(help_text='Preparation time in minutes', null=True, blank=True)
    cooking_time = models.IntegerField(help_text="Cooking time in minutes", null=True, blank=True)
    servings = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']