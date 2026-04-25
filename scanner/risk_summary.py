# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Risk Summary Engine
# =========================================

def calculate_risk_summary(vulnerabilities):
    summary = {
        "total": len(vulnerabilities),
        "high": 0,
        "medium": 0,
        "low": 0,
        "overall_risk": "SAFE"
    }

    for vuln in vulnerabilities:
        risk = vuln.get("risk", "").upper()

        if risk == "HIGH":
            summary["high"] += 1
        elif risk == "MEDIUM":
            summary["medium"] += 1
        elif risk == "LOW":
            summary["low"] += 1

    if summary["high"] > 0:
        summary["overall_risk"] = "HIGH"
    elif summary["medium"] > 0:
        summary["overall_risk"] = "MEDIUM"
    elif summary["low"] > 0:
        summary["overall_risk"] = "LOW"

    return summary
