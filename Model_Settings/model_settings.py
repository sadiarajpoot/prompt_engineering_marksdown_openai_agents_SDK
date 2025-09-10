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

my_agent = Agent(
    name="Assistant",               
    instructions="You are a helpful assistant that solves problems step by step.",
    tools=[add, subtract],
    model_settings=ModelSettings(
        temperature=1,   # zyada creative answer
        max_tokens=100,
        top_p=0.2,
        top_k=3,
        tool_choice="subtract",
        # parallel_tool_calls=True
        # ❌ tool_choice yahan nahi aayega
    )
)

response = Runner.run_sync(
    my_agent,
    "What is 2+2",
    run_config=config   # yahan sirf model provider info hona chahiye
)
print(response.final_output)
