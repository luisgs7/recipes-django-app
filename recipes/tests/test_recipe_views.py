from django.urls import reverse, resolve

# from unittest import skip

from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeViewTest(RecipeTestBase):
    def tearDown(self) -> None:
        return super().tearDown()

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse("recipes:home"))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertTemplateUsed(response, "recipes/pages/home.html")

    # @skip("Mensagem de porque o teste foi pulado")
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertIn(
            "<h1>No recipes found here!</h1>", response.content.decode("utf-8")
        )

        # self.fail("Corrigir o teste...")

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs={"category_id": 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse("recipes:home"))
        content = response.content.decode("utf-8")
        response_context_recipes = response.context["recipes"]

        self.assertIn("Recipe Title", content)
        # self.assertIn("10 Minutos", content)
        # self.assertIn("5 Porções", content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_category_template_loads_recipe(self):
        title = "This is a category test"
        # Title a recipe for this test
        self.make_recipe(title=title)

        response = self.client.get(reverse("recipes:category", args=(1,)))
        content = response.content.decode("utf-8")

        # Check is one recipe exists
        self.assertIn(title, content)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"id": 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse("recipes:recipe", kwargs={"id": 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        need_title = "This is a detail page - it load one recipe"

        self.make_recipe(title=need_title)

        response = self.client.get(reverse("recipes:recipe", kwargs={"id": 1}))

        content = response.content.decode("utf-8")

        self.assertIn(need_title, content)
