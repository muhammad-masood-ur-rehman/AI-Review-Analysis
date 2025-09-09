EXTRACTION_FIELDS = {
    "positive_opinions": "Positive feedback about features, services, or experiences.",
    "negative_opinions": "Negative feedback about features, services, or experiences.",
    "problems": "Explicitly mentioned issues, errors, or pain points.",
    "suggestions": "User-provided solutions, recommendations, or feature requests."
}

def get_review_prompt(review: dict) -> list:
    
    schema_instructions = "\n".join(
        [f"- {field}: {desc}" for field, desc in EXTRACTION_FIELDS.items()]
    )

    schema_text = "\n".join([f'  "{f}": ["..."]' for f in EXTRACTION_FIELDS.keys()])

    system_message = {
        "role": "system",
        "content": (
            "You are an AI assistant that extracts structured, machine-readable insights "
            "from unstructured customer reviews.\n\n"
            "Always output a **valid JSON object** strictly following this schema:\n"
            "{\n"
                f"{schema_text}\n"
            "}\n\n"
            "Each key must always be present. Use empty lists [] if no insights are found.\n"
        )
    }


    user_message = {
        "role": "user",
        "content": f"""
                        Review Details:
                        Review ID: {review.get('review_id')}
                        Date: {review.get('date')}
                        Rating: {review.get('rating')}
                        Text: {review.get('text')}

                        Extraction Instructions:
                        Please extract insights from the review into the following categories:
                        {schema_instructions}
"""
    }

    return [system_message, user_message]
