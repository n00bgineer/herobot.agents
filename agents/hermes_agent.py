from uagents import Agent, Context
from env_config import env

hermes_agent_seed = env.hermes_agent_seed
if not hermes_agent_seed:
  raise Exception("ERROR: HERMES_AGENT_SEED NOT SET IN .env FILE")

HermesAgent = Agent(
    name="HermesAgent",
    port=8003,
    seed=hermes_agent_seed,
    endpoint="http://localhost:8001/agent/hermes",
)

@HermesAgent.on_event("startup")
async def startup_handler(ctx: Context):
  ctx.logger.info(f"STARTUP AGENT://{ctx.agent.name}::{ctx.agent.address}")

if __name__ == "__main__":
  HermesAgent.run()