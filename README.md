# Autonomous AI Avatar Engine

An AI-powered engine designed for script intelligence, content optimization, and action execution.

## System Role
The engine operates as a modular, goal-driven agent capable of understanding instructions, improving scripts, adapting roles, and triggering external actions.

## Core Functions
1. **Script Comprehension**: Parse intent, audience, tone, and platform.
2. **Script Optimization**: Rewrite for clarity, emotion, and flow.
3. **Performance Intelligence**: Suggest delivery style and avatar cues.
4. **Multi-Format Output**: Long-form, short-form, voice-optimized.
5. **Action Planning**: Convert scripts into executable task sequences.
6. **Tool Awareness**: Prepare structured outputs for automation.

## Project Structure
```text
avatar/
├── app/
│   ├── __init__.py
│   ├── main.py            # API Entry point
│   ├── models.py          # Input/Output Pydantic schemas
│   └── engine.py          # Core AI Avatar Engine logic
├── requirements.txt       # Project dependencies
└── README.md              # Documentation
```

## Setup & Usage

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Server**:
    ```bash
    uvicorn app.main:app --reload
    ```

3.  **API Usage**:
    The API will be available at `http://localhost:8000`.
    
    **POST /process**
    
    **Request Body:**
    ```json
    {
      "task_type": "script_analysis",
      "script": "Hello world, this is a test script.",
      "role": "news",
      "platform": "youtube",
      "audience": "general",
      "tone": "energetic",
      "goal": "engagement"
    }
    ```

    **Response:**
    Returns a JSON object containing analysis, optimized script, delivery guidance, and an action plan.
