from uagents import Agent, Context
from env_config import env

# ACCESSING ENVIRONMENT VARIABLES
apollo_agent_seed = env.apollo_agent_seed
apollo_agent_origin = env.apollo_agent_origin
if not apollo_agent_seed:
  raise Exception("ERROR: APOLLO_AGENT_SEED NOT SET IN .env FILE")
if not apollo_agent_origin:
  raise Exception("ERROR: APOLLO_AGENT_ORIGIN NOT SET IN .env FILE")

ApolloAgent = Agent(
    name = "ApolloAgent",
    port = 8002,
    seed = apollo_agent_seed,
    endpoint = apollo_agent_origin + "/agent/apollo",
)

@ApolloAgent.on_event("startup")
async def startup_handler(ctx: Context):
  ctx.logger.info(f"STARTUP AGENT://{ctx.agent.name}::{ctx.agent.address}")

if __name__ == "__main__":
  ApolloAgent.run()