import os
from dotenv import load_dotenv
load_dotenv()

env = {
  "athena_agent_seed": os.getenv("ATHENA_AGENT_SEED"),
  "apollo_agent_seed": os.getenv("APOLLO_AGENT_SEED"),
  "hermes_agent_seed": os.getenv("HERMES_AGENT_SEED"),
  "athena_agent_url": os.getenv("ATHENA_AGENT_URL"),
  "apollo_agent_url": os.getenv("APOLLO_AGENT_URL"),
  "hermes_agent_url": os.getenv("HERMES_AGENT_URL"),
}