FastAPI Query Parameters Example
This project demonstrates how to use query parameters in FastAPI to filter results based on optional inputs such as price and name.

📌 What are Query Parameters?
In FastAPI, query parameters are values passed in the URL after the ? symbol.
They are commonly used for filtering, searching, and sorting data in API endpoints.

For example:http://127.0.0.1:8000/items?price=500&name=laptop
**How it Works**

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items")
async def show_items(price: Optional[int] = None, name: Optional[str] = None):
    return {"price": price, "name": name}

   ** Key Points:**
Optional → Makes parameters optional (default None if not provided).

Order does not matter in query parameters.

If no query parameter is provided, the default values are returned.

Query parameters appear in the Swagger UI under the endpoint.

**Running the Project**
Install FastAPI and Uvicorn:
pip install fastapi uvicorn

**Run the server:**
uvicorn quiz:app --reload

**Open your browser:**
http://127.0.0.1:8000/docs
You can test query parameters directly in Swagger UI.

**Example Requests**
With both parameters:
GET /items?price=500&name=laptop
→ {"price": 500, "name": "laptop"}

**With only one parameter:**
GET /items?price=1000
→ {"price": 1000, "name": null}

**Notes**
Query parameters are great for search filters in APIs.

You can combine them with path parameters for more flexibility.

They are automatically validated if you specify types (int, str, etc.).
