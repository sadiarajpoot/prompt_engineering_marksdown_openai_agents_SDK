from agents import Agent,Runner
from main import config


my_agent = Agent(
    name="math_helper",               
    instructions="You are a helpful assistant that solves math problems step by step."
)


response = Runner.run_sync(my_agent,"What is 5 + 7 * 2 ?",run_config=config)

print(response)