import json
from llm.llm import call_openrouter
from prompts.review import get_review_prompt

input_review = {
        "review_id": "R13579",
        "date": "2025-01-10",
        "rating": "★★★☆☆ (3 stars)",
        "text": ("""The app UI looks good but is confusing to navigate.
        Please make the checkout process simpler."""
        )
    }

    
messages = get_review_prompt(input_review)

raw_output = call_openrouter(messages)

try:
        insights = json.loads(raw_output)
except json.JSONDecodeError:
        insights = {"error": "Invalid JSON from model", "raw_output": raw_output}

    # Pretty print result
print(json.dumps(insights, indent=2))
