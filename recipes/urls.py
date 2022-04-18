from django.urls import path

from recipes.views import home, recipes

app_name = 'recipes'

urlpatterns = [
    path("", home, name="home"),
    path("recipes/<int:id>/", recipes, name="detail")
]
