import sys
from pathlib import Path
from google import genai
from google.genai import types

# INSERTING PARENT PATH
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
from env_config import env
from llm_config import config

def generate():
    client = genai.Client(
        api_key=env["gemini_api_key"],
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""{
  \"subject\": \"JavaScript\",
  \"category\": \"fundamental\",
   \"excluded\": []
}"""),
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type = genai.types.Type.ARRAY,
            items = genai.types.Schema(
                type = genai.types.Type.STRING,
            ),
        ),
        system_instruction=[
            types.Part.from_text(text=config["system_prompt"]),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
