from agents import Agent,Runner,function_tool,enable_verbose_stdout_logging,set_tracing_disabled
from main import config
from pydantic_class import BaseModel
from typing import List,Dict

set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()

class StudentInformation(BaseModel):
    id:int
    user_name:str
    roll_number:int
    subjects:List[str]
    marks:Dict[str,int]
    
try:
    s1=StudentInformation(id=1 , user_name= "Sadia Khan" , roll_number=12345 ,
    subjects=["Math", "Science","English","Urdu","Islamiyat"],
    marks={"Math":"90", "Science":88 , "English": 70}                       
     )
    print("student :" , s1)
except Exception as e:
    print(e)
    


