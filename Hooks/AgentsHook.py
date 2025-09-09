from agents import Agent, AgentHooks, ModelResponse, Runner, TResponseInputItem, enable_verbose_stdout_logging, function_tool, set_tracing_disabled, RunContextWrapper, Tool
from typing import Any, Optional
from main import config

set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()

@function_tool
def get_Weather(city:str) -> int:
    return f"The weather of {city} is Sunny"

math_agent = Agent(
    name="math_teacher",
    instructions="You are a math teacher. Solve math problems step by step.",
    tools=[get_Weather],
    handoff_description="You are a math teacher agent who solve math questions"
)

english_agent = Agent(
    name="english_teacher",
    instructions="You are an English teacher. Help improve grammar and sentences.",
    handoff_description="You are an English teacher agent who solve English questions"
)

class AgentHookClass(AgentHooks):
    async def on_start(self, context: RunContextWrapper, agent: Agent) -> None:
        print("on_start : Agent started ----->")

    async def on_end(self, context: RunContextWrapper, agent: Agent, output: Any) -> None:
        print("on_end : Agent ended ----->")

    async def on_handoff(self, context: RunContextWrapper, agent: Agent, source: Agent) -> None:
        print("on_handoff : Agent handoff ----->")

    async def on_tool_start(self, context: RunContextWrapper, agent: Agent, tool: Tool) -> None:
        print("on_tool_start : Tool started ----->")

    async def on_tool_end(self, context: RunContextWrapper, agent: Agent, tool: Tool, result: str) -> None:
        print("on_tool_end : Tool ended ----->")

    async def on_llm_start(self, context: RunContextWrapper, agent: Agent, system_prompt: Optional[str], input_items: list[TResponseInputItem]) -> None:
        print("on_llm_start : LLM started ----->")

    async def on_llm_end(self, context: RunContextWrapper, agent: Agent, response: ModelResponse) -> None:
        print("on_llm_end : LLM ended ----->")

my_agent = Agent(
    name="support_helper",               
    instructions="You are a helpful assistant that solve problems step by step.",
    handoffs=[math_agent, english_agent],
    tools=[get_Weather],
    hooks=AgentHookClass()
)


response = Runner.run_sync(my_agent, "What is the weather of karachi?", run_config=config)

print(response)
