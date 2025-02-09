
# AI-Powered Q&A Agent

## Project Overview

This project is a small web application that allows users to interact with an AI-powered Q&A agent. The user queries the AI, and the agent responds with relevant answers. The application maintains a history of the conversation to provide context for each query.

## Features

- **Interactive Q&A**: Users can type queries, and the AI responds with relevant answers.
- **Conversation History**: The application maintains a history of interactions, ensuring better context for AI responses.
- **Dynamic UI**: The user interface updates in real-time without requiring a page reload.
- **API Integration**: Backend integrated with an AI/LLM service (e.g., OpenAI GPT) for generating answers.

## Tech Stack

- **Frontend**: React.js (or Vue/Angular as alternatives)
- **Backend**: FastAPI (or Django/Flask/Node.js as alternatives)
- **AI Integration**: OpenAI GPT (or other LLMs)

## Getting Started

### Prerequisites

- Node.js (for frontend)
- Python 3.x (for backend)
- API Key for OpenAI or other LLM service

### Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai_qa_agent.git
cd ai_qa_agent
```

#### 2. Frontend Setup

1. Navigate to the `frontend` directory.

```bash
cd frontend
```

2. Install the required dependencies:

```bash
npm install
```

3. Run the frontend:

```bash
npm start
```

The frontend should now be running on `http://localhost:3000`.

#### 3. Backend Setup

1. Navigate to the `backend` directory.

```bash
cd backend
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
.env\Scriptsctivate   # For Windows
```

3. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your `.env` file with your OpenAI API key (or other LLM credentials).

```bash
OPENAI_API_KEY=your-api-key-here
```

5. Run the backend:

```bash
uvicorn backend.fastapi_server.main:app --reload
```

The backend API will now be running on `http://localhost:8000`.

### Application Flow

- **Frontend**: The user types a query in the input box and clicks the submit button. The query is sent to the backend API, which processes the request, forwards it to the AI service, and returns the response along with the conversation history.
- **Backend**: The backend receives the query, sends it to the AI service (e.g., OpenAI GPT), and returns the response with the updated conversation history.

## Dependencies

### Frontend

- React.js
- Axios (for API calls)
- Other dependencies listed in `frontend/package.json`

### Backend

- FastAPI
- Uvicorn (for running the FastAPI server)
- OpenAI (for interacting with GPT or other AI models)
- Pydantic (for data validation)

Install all backend dependencies with:

```bash
pip install -r backend/requirements.txt
```

## How AI Integration Works

The backend is integrated with OpenAI's GPT model (or a similar LLM). The AI generates responses based on the current query and the conversation history. The conversation history is sent along with the new query to provide context, allowing the AI to respond more accurately.

## Conversation History Management

The backend stores the conversation history temporarily (in-memory) to send the context with each new query. The history includes both user queries and AI responses. This ensures that the AI can consider the entire conversation, providing more relevant and context-aware responses.
