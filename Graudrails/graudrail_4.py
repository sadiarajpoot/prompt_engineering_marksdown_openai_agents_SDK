import asyncio
from typing import Any, Optional
from agents import (
    Agent, Runner, enable_verbose_stdout_logging, set_tracing_disabled,
    input_guardrail, RunContextWrapper, GuardrailFunctionOutput, InputGuardrailTripwireTriggered
)
from main import config

set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()

# Agent that enforces luggage weight rules
Aeroport_agent = Agent(
    name="Aeroport Security Guard",
    instructions=(
        "You are an airport security guard agent. "
        "If customer luggage weight is more than 25KGs, say: "
        "'Customer, you have more than 25 KGs weight, please check it right now'."
    )
)

# Guardrail to run security checks before passing input to the main agent
@input_guardrail
async def security_guard(wrapper: RunContextWrapper, agent: Agent, input: str) -> GuardrailFunctionOutput:
    result = await Runner.run(Aeroport_agent, input, run_config=wrapper.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=True   # Always trips when run
    )

# Main checker agent
main_Checker = Agent(
    name="Main Checker of Airport",
    instructions="You check the customers luggage using the security guard.",
    input_guardrails=[security_guard]  # ✅ plural is correct
)

async def main():
    try:
        response = await Runner.run(
            main_Checker,
            input="my luggage weight is 30KGs",   # Example input
            run_config=config
        )
        print("Response:", response)

    except InputGuardrailTripwireTriggered:
        print("🚨 Guardrail tripped: Luggage over 25KG detected!")
asyncio.run(main())

