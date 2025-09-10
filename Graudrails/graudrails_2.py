import asyncio
from agents import (
    Agent,
    InputGuardrailTripwireTriggered,
    Runner,
    input_guardrail,
    set_tracing_disabled,
    GuardrailFunctionOutput,
    RunContextWrapper
)
from main import config
from pydantic_class import BaseModel

set_tracing_disabled(disabled=True)


class Check_Math_Input(BaseModel):
    is_Math_work: bool
    reason: str


graudrail_agent = Agent(
    name="math_graudrail_agent",
    instructions=(
        "You are a guardrail agent. "
        "If the input is a math question, set is_Math_work=True. "
        "If not, set is_Math_work=False and explain in reason."
    ),
    output_type=Check_Math_Input
)


@input_guardrail
async def Math_Checker(wrapper: RunContextWrapper, agent: Agent, input: str) -> GuardrailFunctionOutput:
    math_output = await Runner.run(graudrail_agent, input, context=wrapper.context,run_config=config)

    return GuardrailFunctionOutput(
        output_info=math_output.final_output,
        tripwire_triggered=not math_output.final_output.is_Math_work,
    )


Math_Agent = Agent(
    name="Math_Agent",
    instructions="You are a math agent. Only solve math-related queries.",
    input_guardrails=[Math_Checker],
)


async def main():
    try:
        # This should NOT trip the guardrail (math question ✅)
        result = await Runner.run(Math_Agent, "Hello, can you help me..what is chemistry?",run_config=config)
        print("Agent Output:", result.final_output)  # ✅ Now prints agent response

    except InputGuardrailTripwireTriggered as e:
        print("Math homework guardrail tripped ❌")
        # print("Reason:", e.guardrail_function_output.output_info.reason)


if __name__ == "__main__":
    asyncio.run(main())
