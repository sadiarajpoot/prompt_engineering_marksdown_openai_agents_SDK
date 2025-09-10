from agents import Agent, AgentHooks, ModelResponse, Runner, TResponseInputItem, enable_verbose_stdout_logging, function_tool, set_tracing_disabled, RunContextWrapper, Tool
from main import config
from pydantic_class import BaseModel

set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()

class UserInfo(BaseModel):
    user_name: str

# Take input from user
user_input = input("Enter Your Name : ")
user_obj = UserInfo(user_name=user_input)

# Dynamic instructions
def dyn_inst(ctx: RunContextWrapper[UserInfo], agent: Agent):
    return f"Hello {ctx.context.user_name}, I am your {agent.name}."

# Create agent
agent = Agent[UserInfo](
    name="Helper Agent",
    instructions=dyn_inst
)

# Run agent
result = Runner.run_sync(
    agent,
    input=user_input,
    run_config=config,
    context=user_obj
)

print(result.final_output)
