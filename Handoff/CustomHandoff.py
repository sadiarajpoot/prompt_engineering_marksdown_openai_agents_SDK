from agents import Agent, Handoff, Runner ,enable_verbose_stdout_logging, handoff,set_tracing_disabled,RunContextWrapper
set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()
from main import config
from pydantic_class import BaseModel

Billing_Agent=Agent(
    name="Billing_Agent",
    instructions="You are a billing agent.Solve a quries related to billing",
    handoff_description="You are a handoff agent related to billing purpose"
)

Refund_Agent=Agent(
    name="Refund_Agent",
    instructions="You are a Refund agent.Solve a quries related to Refund"
)
# -----------------------input_json_schema-------------------------------
class RefundSchemaClass(BaseModel):
    input:str
MySchema=RefundSchemaClass.model_json_schema()
MySchema["additionalProperties"]=False

# --------------------------on_invoke_handoff----------------------------
async def myInvoke_fun(Wrapper:RunContextWrapper,input:str):
    return Refund_Agent


# -------------------------------------------------------
# name_des_override=handoff(
#     tool_name_override="Refund Agent Call",
#     tool_description_override="You are a Refund Agent .Guide to customer related quiries about refund"
# )
    

# -------------------------------------------------------

Refund_Agent_custom_handoff=Handoff(
    agent_name="Refund_Agent",
    tool_name="Refund_Agent",
    tool_description="You are a Refund agent.Solve a quries related to Refund",
    input_json_schema=MySchema,
    on_invoke_handoff=myInvoke_fun

)
Manager_Agent=Agent(
    name="Manager_Agent",
    instructions="You are a Manager Agent Handle the handoff to appropraite agent",
    handoffs=[Billing_Agent,Refund_Agent_custom_handoff]
    
)
result=Runner.run_sync(Manager_Agent,input="I want to refund my money",run_config=config)
print(result.final_output)
print(result.last_agent)