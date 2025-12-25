import base64
from openai import OpenAI

# It is highly recommended to use environment variables for keys
client = OpenAI(api_key="")

def detect_ingredients(image_bytes: bytes) -> str:
    # Convert bytes to base64 string
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    # Correct OpenAI 1.0+ Chat Completion syntax for Vision
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "List the food ingredients in this image as a comma-separated list. Only list the names of the ingredients."},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}
                    }
                ]
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content