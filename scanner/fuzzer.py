# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Input Fuzzer
# =========================================

import requests
from config import DEFAULT_TIMEOUT
from scanner.response_analyzer import analyze_responses
from scanner.reflection_detector import detect_reflection


def get_test_payloads():
    return [
        "' OR '1'='1",
        "<script>alert(1)</script>",
        "../../etc/passwd",
        "\" onerror=alert(1) \"",
        "'; DROP TABLE users; --"
    ]


def fuzz_get_param(base_url, param_name="q"):
    results = []
    payloads = get_test_payloads()

    try:
        base_res = requests.get(base_url, timeout=DEFAULT_TIMEOUT)
        base_response = {
            "status_code": base_res.status_code,
            "response_body": base_res.text
        }
    except:
        base_response = {
            "status_code": 0,
            "response_body": ""
        }

    for payload in payloads:
        test_url = f"{base_url}?{param_name}={payload}"

        try:
            response = requests.get(test_url, timeout=DEFAULT_TIMEOUT)

            test_response = {
                "status_code": response.status_code,
                "response_body": response.text
            }

            analysis = analyze_responses(base_response, test_response)
            reflection = detect_reflection(payload, response.text)

            results.append({
                "payload": payload,
                "status_code": response.status_code,
                "response_length": len(response.text),
                "analysis": analysis,
                "reflection": reflection["message"],
                "reflection_risk": reflection["risk"]
            })

        except requests.exceptions.Timeout:
            results.append({
                "payload": payload,
                "status_code": "TIMEOUT",
                "response_length": 0,
                "analysis": ["Request timed out"],
                "reflection": "No reflection analysis"
            })

    return results
