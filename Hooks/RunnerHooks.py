from typing import Any, Optional
from agents import Agent, ModelResponse, RunContextWrapper, Runner, TResponseInputItem, Tool ,enable_verbose_stdout_logging, function_tool,set_tracing_disabled,RunHooks
set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()
from main import config

@function_tool
def get_Weather(city:str) -> str:
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

class MyRunHooks(RunHooks):
    
    async def on_llm_start(
        self,
        context: RunContextWrapper,
        agent: Agent,
        system_prompt: Optional[str],
        input_items: list[TResponseInputItem],
    ) -> None:
        print("on_llm_start : on_llm_start---------->")

    async def on_llm_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        response: ModelResponse,
    ) -> None:
        print("on_llm_end: on_llm_end---------->")

    async def on_agent_start(self, context: RunContextWrapper, agent: Agent) -> None:
        print("on_agent_start: on_agent_start---------->")

    async def on_agent_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        output: Any,
    ) -> None:
        print(" on_agent_end: on_agent_end----------->")

    async def on_handoff(
        self,
        context: RunContextWrapper,
        from_agent: Agent,
        to_agent: Agent,
    ) -> None:
        print(" on_handoff: on_handoff----------->")

    async def on_tool_start(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: Tool,
    ) -> None:
        print(" on_tool_start: on_tool_start----------->")

    async def on_tool_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: Tool,
        result: str,
    ) -> None:
        print(" on_tool_end :  on_tool_end----------->")

# ✅ Attach hooks at the Runner level, not Agent
my_agent = Agent(
    name="support_helper",               
    instructions="You are a helpful assistant that solve problems step by step.",
    handoffs=[math_agent, english_agent],
    tools=[get_Weather]
)

response = Runner.run_sync(
    my_agent,
    "What is the weather of karachi?",
    run_config=config,
    hooks=MyRunHooks()   # <-- hooks go here
)

print(response)
