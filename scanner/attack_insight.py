# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Attack Insight Engine
# =========================================

def generate_insight(vulnerabilities):
    if not vulnerabilities:
        return ["System appears safe based on current checks."]

    insights = []

    for vuln in vulnerabilities:
        if vuln["type"] == "SQL Injection":
            insights.append(
                "SQL Injection risk detected: Input is not properly sanitized. Attackers may manipulate database queries."
            )

        elif vuln["type"] == "XSS":
            insights.append(
                "XSS risk detected: User input is being reflected without proper encoding. This can lead to script execution in the browser."
            )

    return insights
