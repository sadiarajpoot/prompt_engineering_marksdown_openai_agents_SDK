from agents import Agent,Runner,function_tool,enable_verbose_stdout_logging,set_tracing_disabled
from main import config

set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()


@function_tool
def calculator(a:int,b:int) -> int:
    return a * b

@function_tool
def greet(name: str) -> str:
    """Greet a person by name"""
    return f"Hello {name}, nice to meet you!"

multi_agent = Agent(
    name="multi_purpose",
    instructions="You are a multi-purpose assistant. Use tools when required.",
    tools=[calculator, greet]
)

# Try both tools
response1 = Runner.run_sync(multi_agent,"Calculate 15 * 8",run_config=config)
response2 =Runner.run_sync(multi_agent,"my name is sadia",run_config=config)

print("Math:", response1)
print("Greet:", response2)
