from app.agents.quality_agent import quality_check
from app.agents.security_agent import security_check
from app.agents.bias_agent import bias_check
from app.core.scorer import calculate_score
from app.models.report import Report

def analyze_code(code: str) -> Report:
    quality = quality_check(code)
    security = security_check(code)
    bias = bias_check(code)

    score = calculate_score(quality["score"], security["score"], bias["score"])

    report = Report(
        quality=quality,
        security=security,
        bias=bias,
        score=score
    )
    return report
