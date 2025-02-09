import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API Key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

# In-memory storage for conversation history
conversation_history = []

@app.post("/chat/")
async def chat(request: QueryRequest):
    if not openai.api_key:
        raise HTTPException(status_code=500, detail="OpenAI API key is missing!")

    # Add user's query to conversation history
    conversation_history.append({"role": "user", "content": request.query})

    try:
        # Generate AI's response using OpenAI's GPT model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use other models if needed
            messages=conversation_history
        )

        # Get the AI response and append it to history
        ai_response = response["choices"][0]["message"]["content"]
        conversation_history.append({"role": "assistant", "content": ai_response})

        return {"response": ai_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI Error: {str(e)}")
