from agents import (
    Agent,
    Runner,
    RunContextWrapper,
    input_guardrail,
    GuardrailFunctionOutput,
    TResponseInputItem,
    enable_verbose_stdout_logging,
    set_tracing_disabled
)
from main import config
from pydantic import BaseModel


# Enable logs
# enable_verbose_stdout_logging()
set_tracing_disabled(disabled=True)


class LanguageOutput(BaseModel):
    is_abusive: bool
    reason: str


# Guardrail Agent
guardrail_agent = Agent(
    name="Language_Checker_Guardrail_Agent",
    instructions=(
        "Check the user's input. "
        "If it contains abusive, offensive, or impolite language, "
        "respond with is_abusive=True and explain politely in 'reason'. "
        "Otherwise, respond with is_abusive=False and reason='Looks fine'."
    ),
    output_type=LanguageOutput,
)


# Guardrail Function with try/except
@input_guardrail
def Language_Checker(
    wrapper: RunContextWrapper,
    agent: Agent,
    input: str | TResponseInputItem
) -> GuardrailFunctionOutput:
    try:
        result = Runner.run_sync(guardrail_agent, input=input, context=wrapper)

        return GuardrailFunctionOutput(
            output_info=result.final_output,
            tripwire_triggered=str(result.final_output.is_abusive)
        )

    except Exception as e:
        # Agar koi error aaya toh safe response
        return GuardrailFunctionOutput(
            output_info={"error": str(e)},
            tripwire_triggered="False"
        )


# Main Customer Support Agent
agent = Agent(
    name="Customer Support Agent",
    instructions="You are a customer support agent. You help customers with their questions politely and professionally."
)


# Example Test with try/except
if __name__ == "__main__":
    try:
        polite = Runner.run_sync(agent, input="Hello, I need help with my order.", run_config=config)
        print("Polite Input →", polite.final_output)
    except Exception as e:
        print("Error in polite input:", e)

    try:
        abusive = Runner.run_sync(agent, input="You are stupid!", run_config=config)
        print("Abusive Input →", abusive.final_output)
    except Exception as e:
        print("Error in abusive input:", e)
