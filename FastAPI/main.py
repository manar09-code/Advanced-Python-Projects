#installation FastAPI
#ps: Uvicorn is the server that will be used ti test and run our FastAPI applications.
import curl
from fastapi import FastAPI
# Create an app
app = FastAPI()
# define a path for HTTP Get method
@app.get("/")
def root():
    return {"Hello": "World"}
#to run the server we use "uvicorn"
#GET and POST routes: used to define the different URLs that your app should respond to.
#let’s build a to-do list application. We’ll need different routes to add or view the to-do items on the list.
items = []
#creating a new endpoint
#ps:app Users can access this endpoint by sending an HTTP Post request to this items path, and it’s going to accept item as an input (query parameter).
@app.post("items")
def create_item(item: str):
    items.append(item)
    return item
#testing the endpoint
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple' #in terminal
#creating an endpoint to view  specific item of the list
@app.get("items/{item_id}")
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item
#testing the endpoint
curl -X GET http://127.0.0.1:8000/items/0 #in terminal
#trying to get an item that doesn’t exist
curl -X GET http://127.0.0.1:8000/items/7 #in terminal
#http errors
#to do that we need to import HTTPException from FastAPI
from fastapi import FastAPI, HTTPException
#modifying the get_item() endpoint to use the HTTPException
@app.get("items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return = items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
#running the same request
curl -X GET http://127.0.0.1:8000/items/7 #in terminal
#JSON Request and Path Parameters
#creating a new endpoint called list_items
# this endpoint uses a query parameter 'limit'
@app.get("/items/")
def list_items(limit: int = 10):
    return items[0:limit]
#testing the endpoint
curl -X GET 'http://127.0.0.1:8000/items?limit=3' #in terminal
#Pydantic models
#Pydantic is the most widely used data validation library for Python. It lets you structure your data, gives you type-hints and auto-complete in your IDE, and helps to serialize to and from JSON.
from pydantic import BaseModel
class Item(BaseModel):
    text: str = None
    is_done: bool = False
...
def create_item(item: Item):
...
def get_item(item_id: int) -> Item:
#testing the create_item enndpoint in terminal with
curl -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' 'http://127.0.0.1:8000/items'
#changing the text ttribute of the item class to be required
class Item(BaseModel):
    # without default value
    text: str
    is_done: bool = False
#testing in the terminal with this
curl -X POST -H "Content-Type: application/json" -d '{"title":"apple"}' 'http://127.0.0.1:8000/items'
#response models
# update the app where we list items or where we get the item, all we have to do is add a new argument to the decorator called response_mode
...
# Specify the response type will be a list of Item
@app.get("/items", response_model=list[Item])
def list_item(limit: int = 10):
...
# Specify the response type will be an Item model
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
#==>This is very useful when we want to build a frontend client that interacts with FastAPI because we have a defined response structure.
