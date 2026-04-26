# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Session Security Checker
# =========================================

import requests


def check_session_security(url):
    findings = []

    try:
        response = requests.get(url, timeout=10)

        headers = response.headers
        cookies = headers.get("Set-Cookie", "")

        if not cookies:
            findings.append("No session cookies detected")
        else:
            findings.append("Session cookie detected")

            if "Secure" in cookies:
                findings.append("Secure flag detected")
            else:
                findings.append("Missing Secure flag")

            if "HttpOnly" in cookies:
                findings.append("HttpOnly flag detected")
            else:
                findings.append("Missing HttpOnly flag")

            if "SameSite" in cookies:
                findings.append("SameSite attribute detected")
            else:
                findings.append("Missing SameSite attribute")

    except requests.exceptions.RequestException as e:
        findings.append(f"Request failed: {str(e)}")

    return findings
