import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/matchilling/api/chuck-norris'

mcp = FastMCP('chuck-norris')

@mcp.tool()
def jokes_random(category: Annotated[Union[str, None], Field(description='Specifies the category of the random joke.')] = None) -> dict: 
    '''Retrieve a random chuck joke in JSON format.'''
    url = 'https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random'
    headers = {'accept': 'application/json', 'x-rapidapi-host': 'matchilling-chuck-norris-jokes-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category': category,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def jokes_categories() -> dict: 
    '''Retrieve a list of available joke categories.'''
    url = 'https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/categories'
    headers = {'accept': 'application/json', 'x-rapidapi-host': 'matchilling-chuck-norris-jokes-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def jokes_search(query: Annotated[str, Field(description='The search term.')]) -> dict: 
    '''Free text search'''
    url = 'https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/search'
    headers = {'accept': 'application/json', 'x-rapidapi-host': 'matchilling-chuck-norris-jokes-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
