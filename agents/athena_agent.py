from uagents import Agent, Context
from env_config import env

# ACCESSING ENVIRONMENT VARIABLES
athena_agent_seed = env.athena_agent_seed
athena_agent_origin = env.athena_agent_origin
if not athena_agent_seed:
  raise Exception("ERROR: ATHENA_AGENT_SEED NOT SET IN .env FILE")
if not athena_agent_origin:
  raise Exception("ERROR: ATHENA_AGENT_ORIGIN NOT SET IN .env FILE")

AthenaAgent = Agent(
    name = "AthenaAgent",
    port = 8001,
    seed = athena_agent_origin,
    endpoint = athena_agent_origin + "/agent/athena",
)

@AthenaAgent.on_event("startup")
async def startup_handler(ctx: Context):
  ctx.logger.info(f"STARTUP AGENT://{ctx.agent.name}::{ctx.agent.address}")

if __name__ == "__main__":
  AthenaAgent.run()