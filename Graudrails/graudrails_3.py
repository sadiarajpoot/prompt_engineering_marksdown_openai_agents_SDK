import asyncio
import os
from agents import (
    Agent,
    InputGuardrailTripwireTriggered,
    Runner,
    input_guardrail,
    set_tracing_disabled,
    GuardrailFunctionOutput,
    RunContextWrapper,
    set_tracing_export_api_key
)
from main import config
from pydantic import BaseModel


# ✅ Get API key from environment
openai_api = os.getenv("OPENAI_API_KEY")

# ✅ Set tracing with API key
set_tracing_export_api_key(openai_api)

# ✅ Proper Pydantic model for guardrail output
class MallOutputChecker(BaseModel):
    is_illegal: bool
    advice: str

graudrail_agent = Agent(
    name="Mall_Guardrail_Agent",
    instructions="You are a Mall Guardrail Agent. Check and validate that the customer does not bring illegal items into the mall."
)

@input_guardrail
async def Mall_Checker(wrapper: RunContextWrapper, agent: Agent, user_input: str) -> GuardrailFunctionOutput:
    Mall_Check_result = await Runner.run(
        graudrail_agent,
        user_input,
        context=wrapper.context,
        run_config=config
    )

    # ✅ Convert result into MallOutputChecker model
    try:
        output = MallOutputChecker.parse_obj(Mall_Check_result.final_output)
    except Exception:
        # Fallback if output is not structured as expected
        output = MallOutputChecker(is_illegal=False, advice="All good")

    return GuardrailFunctionOutput(
        output_info=output,
        tripwire_triggered=output.is_illegal
    )

# ✅ Main agent with guardrail attached
Sadia_Mall_Agent = Agent(
    name="Sadia_Mall_Agent",
    instructions="You are Sadia Mall Agent. Check the entry customer. Customers must not bring illegal things.",
    input_guardrails=[Mall_Checker]
)

async def main():
    try:
        # This should NOT trip the guardrail
        result = await Runner.run(Sadia_Mall_Agent, "Hello, can you help me..what is chemistry?", run_config=config)
        print("Agent Output:", result.final_output)

    except InputGuardrailTripwireTriggered as e:
        print("Mall guardrail tripped ❌")
        print("Reason:", e.guardrail_function_output.output_info.advice)


if __name__ == "__main__":
    asyncio.run(main())
