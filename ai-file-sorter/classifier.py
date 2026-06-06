from ollama import chat
import json


def classify(text, existing_folders):

    prompt = f"""
You are organizing files.

Existing folders:
{", ".join(existing_folders)}

Choose the BEST matching folder from the existing folders.

Return ONLY valid JSON.

{{
  "folder": "folder name",
  "reason": "short explanation"
}}

Do not include markdown.
Do not include code fences.
Return only JSON.

File content:

{text[:2000]}
"""

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    print("\nRAW AI RESPONSE:")
    print(content)

    try:
        return json.loads(content)

    except Exception:

        return {
            "folder": "Other",
            "reason": "Failed to parse AI response"
        }