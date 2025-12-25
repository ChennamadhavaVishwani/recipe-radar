import requests

BASE_URL = "https://www.themealdb.com/api/json/v1/1"

def get_recipes_by_ingredients(ingredients, limit=5):
    meals_found = {}

    for ingredient in ingredients:
        url = f"{BASE_URL}/filter.php?i={ingredient}"
        response = requests.get(url)

        if response.status_code != 200:
            continue

        data = response.json()
        if not data.get("meals"):
            continue

        for meal in data["meals"]:
            meals_found[meal["idMeal"]] = {
                "id": meal["idMeal"],
                "name": meal["strMeal"],
                "image": meal["strMealThumb"]
            }

    return list(meals_found.values())[:limit]
