from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging, ModelSettings
from main import config

# enable_verbose_stdout_logging()

@function_tool
def add(a: int, b: int) -> int:
    """Add two integers"""
    return a + b

@function_tool
def subtract(a: int, b: int) -> int:
    """Subtract two integers"""
    return a - b

# Base Settings
base_settings= ModelSettings(
    temperature=1,
    max_tokens=5,
    top_p=0.5,
    top_k=2,
    # tool_choice="subtract"
)

# overide Settings
overide_settings= ModelSettings(
    temperature=0.1,
    max_tokens=15,
    top_p=0.3,
    top_k=5,
    # tool_choice="add"
)
# overide Settings
final_settings=base_settings.resolve(overide_settings)

my_agent = Agent(
    name="Assistant",               
    instructions="You are a helpful assistant that solves problems step by step.",
    # tools=[add, subtract],
    model_settings=final_settings
)

response = Runner.run_sync(
    my_agent,
    "What is Chemistry",
    run_config=config
)
print(response.final_output)