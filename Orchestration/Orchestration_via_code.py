from agents import Agent,Runner,function_tool,enable_verbose_stdout_logging,set_tracing_disabled
from main import config

set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()

Researcher = Agent(
    name="Researcher",
    instructions="Make a concise bullet outline for the given topic."
)
Writer = Agent(
    name="Writer",
    instructions="Write a 3-paragraph draft based on the provided outline."
)
Reviewer = Agent(
    name="Reviewer",
    instructions="Critique the draft and suggest improvements in bullets."
)

topic = "Benefits and risks of AI in healthcare"

outline_res = Runner.run_sync(Researcher, input=topic)
draft_res = Runner.run_sync(Writer, input=f"Outline:\n{outline_res.final_output}")
review_res = Runner.run_sync(Reviewer, input=f"Draft:\n{draft_res.final_output}")

print("Outline:\n", outline_res.final_output)
print("Draft:\n", draft_res.final_output)
print("Review:\n", review_res.final_output)
