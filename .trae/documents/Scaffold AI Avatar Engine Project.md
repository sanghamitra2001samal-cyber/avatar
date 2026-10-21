Based on the system role and specifications you provided, I will scaffold the **AI Avatar Engine** project. Since the current directory is empty, I will set up a modular Python-based architecture (using FastAPI) that implements the defined core functions and data structures.

### Project Structure
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

### Implementation Steps

1.  **Define Data Models (`app/models.py`)**
    *   Create Pydantic models for `InputObject` (task_type, script, role, etc.) and `OutputObject` (analysis, optimized_script, delivery_guidance, action_plan) to ensure strict typing and validation.

2.  **Implement Core Engine (`app/engine.py`)**
    *   Create the `AvatarEngine` class.
    *   Implement stub methods for the core functions: `analyze_script`, `optimize_script`, `generate_delivery_guidance`, and `create_action_plan`.
    *   Ensure the `process` method orchestrates these steps to transform Input to Output.

3.  **Setup API (`app/main.py`)**
    *   Initialize a FastAPI application.
    *   Create a POST endpoint `/process` that accepts the `InputObject` and returns the `OutputObject` using the `AvatarEngine`.

4.  **Dependencies & Documentation**
    *   Create `requirements.txt` (fastapi, uvicorn, pydantic, etc.).
    *   Create `README.md` with usage instructions and the System Role description.

This foundation will allow you to expand the logic (connecting to actual LLMs or external tools) while adhering to the specified input/output contracts.