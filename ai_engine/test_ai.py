from ai_engine.engine import get_recommendation


user_input = {
    "crop": "tomato",
    "soil": "loamy",
    "stage": "flowering",
    "weather": "normal"
}

result = get_recommendation(user_input)

print(result)