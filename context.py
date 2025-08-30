from agents import Agent,Runner,function_tool,enable_verbose_stdout_logging,set_tracing_disabled,RunContextWrapper
from main import config
from pydantic import BaseModel

set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()

class User (BaseModel):
    name:str
    age:int
    roll_number:str

UserOne=User(name="Sadia Khan" , age=19 , roll_number="123456" )

def Dynamic_instruction_user(Wrapper:RunContextWrapper[User],agent:Agent):
    Wrapper.context.name="Nadia Khan"
    return f"My name is {Wrapper.context.name} and age is {Wrapper.context.age} and roll number is {Wrapper.context.roll_number}"

my_agent = Agent[User](
    name="math_helper",               
    instructions=Dynamic_instruction_user
)
response = Runner.run_sync(my_agent,"What is the name of user",run_config=config, context=UserOne)
print(response)