from pydantic import validator, BaseModel, EmailStr
import re

class Sectors(BaseModel): 
    id: int 
    sector_name: str