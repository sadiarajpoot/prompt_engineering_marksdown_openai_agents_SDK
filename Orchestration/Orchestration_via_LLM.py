from agents import Agent, handoff, Runner, set_tracing_disabled, enable_verbose_stdout_logging
from main import config

set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()

# enable_verbose_stdout_logging()  # debugging ke liye on kar saktay ho

# 1) Specialist agents
Billing_Agent = Agent(
    name="Billing_Agent",
    instructions="You are a billing agent. Solve queries related to billing."
)

Refund_Agent = Agent(
    name="Refund_Agent",
    instructions="You are a refund agent. Solve queries related to refunds."
)

# 2) Handoffs wrap (LLM ko yeh tools dikhte hain)
Billing_Handoff = handoff(
    agent=Billing_Agent,
    name="Billing Agent Call",
    description="Handle billing-related questions."
)
Refund_Handoff = handoff(
    agent=Refund_Agent,
    name="Refund Agent Call",
    description="Handle refund-related questions."
)

# 3) Manager agent (sirf handoffs list do; LLM khud choose karega)
Manager_Agent = Agent(
    name="Manager_Agent",
    instructions=(
        "You are a manager. Read the user request and use the correct handoff tool: "
        "use Billing Agent Call for billing; use Refund Agent Call for refunds."
    ),
    handoffs=[Billing_Handoff, Refund_Handoff]
)

# 4) Run
result = Runner.run_sync(Manager_Agent, input="I want to refund my money")
print("Final Output:", result.final_output)
print("Last Agent:", result.last_agent)
