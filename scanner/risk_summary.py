# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Advanced Risk Summary Engine
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


def generate_risk_summary(issues):
    summary = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0,
        "Safe": 0
    }

    for issue in issues:
        issue_text = str(issue).lower()

        if any(word in issue_text for word in [
            "sql injection",
            "authentication bypass",
            "critical"
        ]):
            summary["Critical"] += 1

        elif any(word in issue_text for word in [
            "xss",
            "high",
            "jwt",
            "session hijacking"
        ]):
            summary["High"] += 1

        elif any(word in issue_text for word in [
            "missing security header",
            "token",
            "medium",
            "csrf"
        ]):
            summary["Medium"] += 1

        elif any(word in issue_text for word in [
            "low",
            "information disclosure",
            "reflected"
        ]):
            summary["Low"] += 1

        else:
            summary["Safe"] += 1

    total = sum(summary.values())

    if summary["Critical"] > 0:
        overall = "CRITICAL ATTENTION REQUIRED"
    elif summary["High"] > 0:
        overall = "HIGH RISK DETECTED"
    elif summary["Medium"] > 0:
        overall = "MEDIUM REVIEW RECOMMENDED"
    elif summary["Low"] > 0:
        overall = "LOW RISK OBSERVED"
    else:
        overall = "SAFE"

    return {
        "total_issues": total,
        "summary": summary,
        "overall_status": overall
    }
