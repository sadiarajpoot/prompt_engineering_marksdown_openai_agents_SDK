from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging, set_tracing_disabled
from main import config
from pydantic import BaseModel


set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()

class Weather(BaseModel):
    temperature: float
    city: str
    conditions: str

weather_agent = Agent(
    name="weather_bot",
    instructions="Provide weather details of a city",
    output_type=Weather
)
response = Runner.run_sync(weather_agent, input="What is the weather of Karachi ?" , run_config=config)
print(response.final_output)
