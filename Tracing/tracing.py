import os
from agents import Agent, Runner, set_tracing_export_api_key
from main import config   # ye RunConfig object hai

# ✅ Get API key from environment
openai_api = os.getenv("OPENAI_API_KEY")

# ✅ Set tracing with API key
set_tracing_export_api_key(openai_api)

# ✅ Define agent
my_agent = Agent(
    name="math_helper",
    instructions="You are a helpful assistant that solves math problems step by step."
)

# ✅ Run agent with run_config
response = Runner.run_sync(
    my_agent,
    "What is chemistry ?",
    run_config=config
)

print(response)
