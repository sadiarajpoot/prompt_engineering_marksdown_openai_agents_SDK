from agents import Agent, Runner ,enable_verbose_stdout_logging,set_tracing_disabled
set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()
from main import config

# Step 2: Math Agent
math_agent = Agent(
    name="math_teacher",
    instructions="You are a math teacher. Solve math problems step by step.",
    handoff_description="Your are a math teacher agent who solve math questions" # combine with defult handoff description
)

# Step 3: English Agent
english_agent = Agent(
    name="english_teacher",
    instructions="You are an English teacher. Help improve grammar and sentences.",
    handoff_description="Your are a English teacher agent who solve English questions"
)

# Step 4: Router Agent (decides where to send the question)
router_agent = Agent(
    name="router",
    instructions="""
    You are a router. Understand the student's question.
    - If it is a math problem → hand it off to math_teacher.
    - If it is about English grammar → hand it off to english_teacher.
    """,
    handoffs=[math_agent,english_agent]
)

# Step 5: Test the handoff system
response1 = Runner.run_sync(router_agent,input="Solve 12 * 8 + 5",run_config=config)
print("Math Response:", response1.last_agent.name)

response2 = Runner.run_sync(router_agent,input="Improve this sentence: 'He go to school yesterday'",run_config=config)
print("English Response:", response2.last_agent.name)


response3 = Runner.run_sync(router_agent,input="hello",run_config=config)
print(response3.last_agent.name)
