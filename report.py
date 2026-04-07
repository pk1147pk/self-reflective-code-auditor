from pydantic import BaseModel
from typing import Dict, Any

class Report(BaseModel):
    quality: Dict[str, Any]
    security: Dict[str, Any]
    bias: Dict[str, Any]
    score: float
