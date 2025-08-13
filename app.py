
from fastapi import FastAPI
from inference import get_fault_diagnosis

app = FastAPI(title="LLM-powered Industrial Fault Detection & Maintenance Advisor")

@app.get("/")
def home():
    return {"message": "Fault Detection API is running"}

@app.post("/diagnose")
def diagnose(input_text: str):
    result = get_fault_diagnosis(input_text)
    return {"diagnosis": result}
