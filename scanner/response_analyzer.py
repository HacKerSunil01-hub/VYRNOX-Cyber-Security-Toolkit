# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Response Analyzer
# =========================================

def analyze_responses(base_response, test_response):
    analysis = []

    # Status code comparison
    if base_response["status_code"] != test_response["status_code"]:
        analysis.append("Status code changed after payload injection")

    # Response length comparison
    base_len = len(base_response["response_body"])
    test_len = len(test_response["response_body"])

    if abs(base_len - test_len) > 50:
        analysis.append("Significant response length difference detected")

    return analysis
