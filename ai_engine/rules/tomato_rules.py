rules = [

    {
        "conditions": {
            "crop": "tomato",
            "soil": "loamy"
        },
        "result": {
            "suitability": "high",
            "recommendation": "Tomato is suitable for loamy soil."
        }
    },

    {
        "conditions": {
            "crop": "tomato",
            "soil": "clay",
            "drainage": "poor"
        },
        "result": {
            "alert": "Improve drainage before planting."
        }
    },

    {
        "conditions": {
            "crop": "tomato",
            "stage": "flowering"
        },
        "result": {
    "growth_stage": "Flowering",
    "recommendation": "Monitor soil moisture and crop condition during flowering."
}
    },

   {
    "conditions": {
        "crop": "tomato",
        "stage": "vegetative"
    },
    "result": {
        "growth_stage": "Vegetative",
        "recommendation": "Follow a soil-test-based nutrient and fertilizer plan and monitor plant growth."
    }
},
    {
        "conditions": {
            "crop": "tomato",
            "weather": "heavy rain"
        },
        "result": {
            "alert": "Avoid unnecessary irrigation and monitor drainage."
        }
    },

    {
        "conditions": {
            "crop": "tomato",
            "weather": "hot"
        },
        "result": {
    "irrigation": "Monitor soil moisture regularly and adjust irrigation according to soil moisture and weather conditions."
}
    }
]