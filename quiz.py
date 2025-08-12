from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID, uuid4
from typing import Optional

app = FastAPI()

@app.get("/hello")
async def Home():
    return {"message":"Hello, World!"}

class Items(BaseModel):
    id:UUID = Field(default_factory=uuid4)
    user_id:int
    name:str
    price:float

items_list =[]    

@app.post("/items/")
async def enter_items(item:Items):
    items_list.append(item)
    return {"message":"items entered successfully"}

@app.get("/items/{user_id}")
async def get_userid(user_id:int):
    for item in items_list:
        if item.user_id == user_id:
            return {"user_id":item.user_id,
                    "user_name":f"user_{user_id}"}



@app.get("/myitems/")
async def show_items(price:Optional[int] = None,name:Optional[str]=None):
    filter_items = items_list

    if price is not None:
          filter_items = [item for item in filter_items if item.price == price]
    

    if name is not None:
        filter_items =   [item for item in filter_items if item.name == name]

    return   [item.dict() for item in filter_items]
    


            



