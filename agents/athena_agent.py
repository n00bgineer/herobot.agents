import os
from dotenv import load_dotenv
from uagents import Agent, Context

load_dotenv()
athena_agent_seed = os.environ.get("ATHENA_AGENT_SEED")
if not athena_agent_seed:
  raise Exception("ERROR: ATHENA_AGENT_SEED NOT SET IN .env FILE")

AthenaAgent = Agent(
    name="AthenaAgent",
    port=8001,
    seed=athena_agent_seed,
    endpoint="http://localhost:8001/agent/athena",
)

@AthenaAgent.on_event("startup")
async def startup_handler(ctx: Context):
  ctx.logger.info(f"STARTUP AGENT://{ctx.agent.name}::{ctx.agent.address}")

if __name__ == "__main__":
  AthenaAgent.run()