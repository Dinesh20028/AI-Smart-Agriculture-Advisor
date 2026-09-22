from ai_engine.rules.tomato_rules import rules
from ai_engine.unification.matcher import match_rule
from ai_engine.reasoning.default_reasoning import apply_default_reasoning


def get_recommendation(user_input):

    matched_results = []

    for rule in rules:

        conditions = rule["conditions"]

        if match_rule(user_input, conditions):
            matched_results.append(rule["result"])

    reasoning = apply_default_reasoning(user_input)

    return {
        "matched_results": matched_results,
        "reasoning": reasoning
    }