def apply_default_reasoning(user_input):

    missing_information = []

    required_fields = ["soil", "stage"]

    for field in required_fields:

        if field not in user_input or not user_input[field]:
            missing_information.append(field)

    if missing_information:

        recommendation = ""

        # Default recommendation based on the information available
        if user_input.get("crop") == "tomato":

            recommendation = (
                "Tomato has been selected. "
                "Please check soil condition and growth stage "
                "before making a detailed farming decision."
            )

        else:

            recommendation = (
                "Please provide more crop information "
                "for a detailed recommendation."
            )

        return {
            "type": "default",
            "message": "Some information is missing. The system is using default reasoning.",
            "recommendation": recommendation,
            "missing": missing_information
        }

    return {
        "type": "complete",
        "message": "Complete information is available.",
        "recommendation": ""
    }