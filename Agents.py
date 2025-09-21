from agents import Agent,Runner,ModelSettings
from main import config
from pydantic import BaseModel


class User(BaseModel):
    name:str
    id:int

u=User(name="1234",id="234")

print(type(u.id))
print(u.name)
print(type(u.name))
my_agent = Agent(
    name="math_helper",               
    instructions="You are a helpful assistant that solves math problems step by step.",
    model_settings=ModelSettings(
        temperature=0.7,
        top_p=1
    )
)


response = Runner.run_sync(my_agent,"Hi",run_config=config)

print(response.final_output)