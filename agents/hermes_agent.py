import os
from dotenv import load_dotenv
from uagents import Agent, Context

load_dotenv()
hermes_agent_seed = os.environ.get("HERMES_AGENT_SEED")
if not hermes_agent_seed:
  raise Exception("ERROR: HERMES_AGENT_SEED NOT SET IN .env FILE")

HermesAgent = Agent(
    name="HermesAgent",
    port=8001,
    seed=hermes_agent_seed,
    endpoint="http://localhost:8001/agent/apollo",
)

@HermesAgent.on_event("startup")
async def startup_handler(ctx: Context):
  ctx.logger.info(f"STARTUP AGENT://{ctx.agent.name}::{ctx.agent.address}")

if __name__ == "__main__":
  HermesAgent.run()