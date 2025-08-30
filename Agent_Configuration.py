from agents import Agent,Runner,function_tool,enable_verbose_stdout_logging,set_tracing_disabled
from main import config

set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()

@function_tool
def calculator(a:int,b:int) -> int:
    return a + b



# Agent configuration with tool
science_tutor = Agent(
    name="math_tutor",
    model="gpt-4o-mini",
    instructions="Tum ek math tutor ho. Zaroorat ho to calculator use karo.",
    tools=[calculator]   
)

response =Runner.run_sync(science_tutor,input="Solve 6+6",run_config=config)
print(response)
