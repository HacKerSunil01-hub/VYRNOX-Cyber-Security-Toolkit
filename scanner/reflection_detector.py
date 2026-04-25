# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Reflection Detector
# =========================================

def detect_reflection(payload, response_text):
    response_lower = response_text.lower()
    payload_lower = payload.lower()

    dangerous_patterns = [
        "<script>",
        "javascript:",
        "onerror=",
        "alert("
    ]

    if payload_lower in response_lower:
        risk = "LOW"

        for pattern in dangerous_patterns:
            if pattern in payload_lower:
                risk = "HIGH"
                break

        return {
            "reflected": True,
            "message": "Payload reflected in response",
            "risk": risk
        }

    return {
        "reflected": False,
        "message": "No payload reflection detected",
        "risk": "SAFE"
    }
