from agents import Agent,Runner,function_tool,enable_verbose_stdout_logging,set_tracing_disabled
from main import config
from pydantic import BaseModel

set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()

class UserInformation(BaseModel):
    user_name:str
    age:int
    roll_number:str


try:
    user1=UserInformation(user_name="Sadia Khan" , age= 18 , roll_number="12345")
    # print("User Information",user1)
    print(" COPY :",user1.copy()) 
    print(" JSON :",user1.json())
    print(" DICT :",user1.dict()) 
except Exception as e:
    print("Error",e)


