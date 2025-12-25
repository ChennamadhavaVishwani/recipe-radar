from fastapi import FastAPI, UploadFile, File
from .vision import detect_ingredients
from .recipes import get_recipes_by_ingredients # Assuming recipes.py is in the same folder

app = FastAPI()

@app.post("/api/detect-ingredients")
async def detect(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        
        # 1. Detect ingredients (Returns: "Tomato, Cheese, Basil")
        ingredients_str = detect_ingredients(image_bytes)
        
        # 2. Convert to list: ["Tomato", "Cheese", "Basil"]
        ingredients_list = [i.strip() for i in ingredients_str.split(",")]
        
        # 3. Fetch recipes from ThemealDB logic
        recipes = get_recipes_by_ingredients(ingredients_list)
        
        return {
            "status": "success",
            "detected": ingredients_list,
            "recipes": recipes
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}