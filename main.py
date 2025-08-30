from agents import Agent,OpenAIChatCompletionsModel,AsyncOpenAI,Runner,RunConfig
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY=os.getenv("GEMINI_API_KEY")
if not API_KEY :
    raise ValueError("API_KEY is missing ........")

external_client=AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)
config=RunConfig(
    model=model,
    model_provider=external_client
)
