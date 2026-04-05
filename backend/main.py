from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai import analyze_ticket, auto_resolve

app = FastAPI()

origins = [
    "http://localhost:8501",  
    "http://127.0.0.1:8501"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/ticket")
def create_ticket(text: str):
    auto = auto_resolve(text)
    if auto:
        return {"status": "Auto Resolved", "solution": auto}

    result = analyze_ticket(text)
    return {"status": "Assigned", "analysis": result}