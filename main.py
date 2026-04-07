from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Self-Reflective Agentic AI Code Auditor")

class CodeInput(BaseModel):
    code: str

@app.post("/analyze")
def analyze(payload: CodeInput):
    code = payload.code.lower()

    issues = []
    if "print(" in code or "printf(" in code or "system.out.println(" in code:
        issues.append("Debug print found")

    score = 100 - len(issues) * 10

    return {
        "score": score,
        "issues": issues
    }

