from agents import Agent, AgentHooks, ModelResponse, Runner, TResponseInputItem, enable_verbose_stdout_logging, function_tool, set_tracing_disabled, RunContextWrapper, Tool

from main import config
from pydantic import BaseModel

set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()

class UserInfo(BaseModel):
    name:str
    age:int
    roll_no:str

class UserName (BaseModel):
    input:input

user_name=input("What is your name ?")
user_obj=UserName (name="Sadia Khan",age=19,roll_no="12345")

def dynamic_instructions(Wrapper:RunContextWrapper[UserName],agent:Agent):
    return f"Your are a Home Work Assistant.(Dynamic Instructions) {agent.name}"
    # return f"hello my name is {Wrapper.context.name} age is {Wrapper.context.age} roll no is {Wrapper.context.roll_no}"

HomeWorkAgent=Agent[UserName](
    name="Home Work Agent",
    # instructions="Your are a Home Work Assistant." simple instructions
    instructions=dynamic_instructions
)
result=Runner.run_sync(HomeWorkAgent,input="what is the name of User?" , run_config=config,context=user_obj)
print(result.final_output)