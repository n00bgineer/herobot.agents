
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
import sys
import logging
from pathlib import Path
from google import genai
from google.genai import types
from env_config import env
from llm_config import config

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

MODEL_NAME = "gemini-2.0-flash-lite"

def call_gemini_api(subject, category, excluded):
    """ CALLS THE GEMINI API AND HANDLES RETRIES ON FAILURE """
    client = genai.Client(api_key=env["gemini_api_key"])

    # SETTING SYSTEM MESSAGE AND OUTPUT STRUCTURE
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type=genai.types.Type.ARRAY,
            items=genai.types.Schema(type=genai.types.Type.STRING),
        ),
        system_instruction=[types.Part.from_text(text=config["system_prompt"])],
    )

    # SETTING USER PROMPT
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""{{
                  "subject": "{subject}",
                  "category": "{category}",
                  "excluded": {excluded}
                }}"""),
            ],
        ),
    ]

    try:
        response = client.models.generate_content_stream(
            model=MODEL_NAME,
            contents=contents,
            config=generate_content_config,
        )
        topics = []
        for chunk in response:
            topics.append(chunk.text)
        return topics
    
    except Exception as e:
        logging.error(f"API CALL FAILED: {e}")

    return []

def generate():
    """ Fetches fundamental and intermediate concepts for JavaScript. """
    subject = "JavaScript"
    fundamental_topics = call_gemini_api(subject, "fundamental", [])
    intermediate_topics = call_gemini_api(subject, "intermediate", fundamental_topics)
    print({
        "fundamental": fundamental_topics,
        "intermediate": intermediate_topics,
    })

if __name__ == "__main__":
    generate()
