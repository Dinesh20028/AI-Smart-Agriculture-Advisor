from django.shortcuts import render
from ai_engine.engine import get_recommendation


def home(request):

    result = None

    if request.method == "POST":

        user_input = {
            "crop": request.POST.get("crop"),
            "soil": request.POST.get("soil"),
            "stage": request.POST.get("stage"),
            "weather": request.POST.get("weather"),
        }

        result = get_recommendation(user_input)

    return render(request, "advisor/home.html", {
        "result": result
    })