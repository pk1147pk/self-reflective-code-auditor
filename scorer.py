def calculate_score(quality_score, security_score, bias_score):
    return round((quality_score + security_score + bias_score) / 3, 2)
