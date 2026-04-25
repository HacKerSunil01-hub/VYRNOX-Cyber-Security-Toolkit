# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Vulnerability Scanner
# =========================================

def scan_response(response_text):
    vulnerabilities = []

    response_lower = response_text.lower()

    # 🔴 SQL Injection (OWASP A03)
    sql_patterns = [
        "sql syntax",
        "mysql",
        "syntax error",
        "unexpected token",
        "query failed"
    ]

    for pattern in sql_patterns:
        if pattern in response_lower:
            vulnerabilities.append({
                "type": "SQL Injection",
                "risk": "HIGH",
                "owasp": "A03: Injection",
                "message": f"Possible SQL-related error detected: {pattern}"
            })

    # 🟡 XSS (OWASP A03)
    xss_patterns = [
        "<script>",
        "javascript:",
        "onerror=",
        "alert("
    ]

    for pattern in xss_patterns:
        if pattern in response_lower:
            vulnerabilities.append({
                "type": "XSS",
                "risk": "MEDIUM",
                "owasp": "A03: Injection",
                "message": f"Possible XSS pattern detected: {pattern}"
            })

    return vulnerabilities
