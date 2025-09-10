from agents import Agent,Runner,function_tool,enable_verbose_stdout_logging,set_tracing_disabled
from main import config
from pydantic.dataclasses import dataclass

set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()

@dataclass
class UserInformation:
    user_name:str
    age:int
    roll_number:str

try:
    user1=UserInformation(user_name="Sadia Khan" , age= 18 , roll_number="12345")
    print(user1)
    # print(user1.copy()) Error (dataclass mai copy() method nahi hota)
    # print(user1.json()) Error (dataclass mai json() method nahi hota)
    # print(user1.dict()) Error (dataclass mai dict() method nahi hota)
except Exception as e:
    print("Error",e)
