import os
from dotenv import load_dotenv
load_dotenv()

env = {
  "athena_agent_seed": os.getenv("ATHENA_AGENT_SEED"),
  "apollo_agent_seed": os.getenv("APOLLO_AGENT_SEED"),
  "hermes_agent_seed": os.getenv("HERMES_AGENT_SEED"),
  "athena_agent_origin": os.getenv("ATHENA_AGENT_ORIGIN"),
  "apollo_agent_origin": os.getenv("APOLLO_AGENT_ORIGIN"),
  "hermes_agent_origin": os.getenv("HERMES_AGENT_ORIGIN"),
  "gemini_api_key": os.getenv("GEMINI_API_KEY"),
}