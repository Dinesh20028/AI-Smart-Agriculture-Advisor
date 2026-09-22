def match_rule(user_input, rule_conditions):

    for key, value in rule_conditions.items():

        # If required information is missing
        if key not in user_input:
            return False

        # Compare the user's value with the rule value
        if user_input[key].lower() != value.lower():
            return False

    return True