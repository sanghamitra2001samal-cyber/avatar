from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.models import InputObject, OutputObject
from app.engine import AvatarEngine

app = FastAPI(
    title="Autonomous AI Avatar Engine",
    description="API for script intelligence, content optimization, and action execution.",
    version="1.0.0"
)

engine = AvatarEngine()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def root():
    return FileResponse("app/static/index.html")

@app.post("/process", response_model=OutputObject)
async def process_task(input_data: InputObject):
    try:
        result = await engine.process(input_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
