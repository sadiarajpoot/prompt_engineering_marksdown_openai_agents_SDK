import asyncio
from agents import Agent,Runner,function_tool,enable_verbose_stdout_logging,set_tracing_disabled,RunContextWrapper
from main import config
from openai.types.responses import ResponseTextDeltaEvent


set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()

async def main():
    agent = Agent(
        name="Joker",
        instructions="You are a helpful assistant.",
    )

    result = Runner.run_streamed(agent, input="Please tell me 5 jokes.",run_config=config)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

asyncio.run(main())