# Django Shell

python manage.py shell

from recipes.models import Recipe, Category
categories = Category.objects.all()
categories[0]
categories.order_by('-id')

recipes = Recipe.objects.all()
for recipe in recipes: print(recipe.id, recipe.title)
for recipe in recipes.order_by('-id'): print(recipe.id, recipe.title)
recipes.order_by('-id').first()
recipe._meta.get_fields()
recipe._meta.get_fields()[0]
getattr(recipe, recipe._meta.get_fields()[0].name)
getattr(recipe, 'id')

new_category = Category()
new_category.name = 'café da manhã'
new_category.save()
new_category.id

new_category = Category.objects.create()
new_category = Category.objects.create(name = 'Django Shell')

consulta = Category.objects.get(id=2)
consulta.delete()

categories = Category.objects.filter(id=3)

# Criar usuários pelo django shell
from django.contrib.auth.models import User

User.objects.create_user(first_name="Pedro", last_name="José", username="pedrojose2", email="pedro@gmail.com", password="123456")
