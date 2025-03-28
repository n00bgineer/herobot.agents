import os
from dotenv import load_dotenv
from uagents import Agent, Context

load_dotenv()
apollo_agent_seed = os.environ.get("APOLLO_AGENT_SEED")
if not apollo_agent_seed:
  raise Exception("ERROR: APOLLO_AGENT_SEED NOT SET IN .env FILE")

ApolloAgent = Agent(
    name="ApolloAgent",
    port=8001,
    seed=apollo_agent_seed,
    endpoint="http://localhost:8001/agent/apollo",
)

@ApolloAgent.on_event("startup")
async def startup_handler(ctx: Context):
  ctx.logger.info(f"STARTUP AGENT://{ctx.agent.name}::{ctx.agent.address}")

if __name__ == "__main__":
  ApolloAgent.run()