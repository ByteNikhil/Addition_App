# api.py - FastAPI Backend
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app instance
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Request model for input validation
class NumberInput(BaseModel):
    a: float
    b: float

# GET endpoint for adding two numbers
@app.get("/content")
def add_numbers(a: float, b: float):
    """
    Endpoint to add two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        dict: Result of addition
    """
    result = a + b
    return {"result": result}
