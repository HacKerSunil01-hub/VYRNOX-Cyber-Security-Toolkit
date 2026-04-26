# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Security Header Checker
# =========================================

import requests


def check_security_headers(url):
    findings = []

    important_headers = {
        "Content-Security-Policy": "Missing CSP (Content Security Policy)",
        "Strict-Transport-Security": "Missing HSTS protection",
        "X-Frame-Options": "Missing Clickjacking protection",
        "X-Content-Type-Options": "Missing MIME-sniffing protection",
        "Referrer-Policy": "Missing Referrer Policy",
        "Permissions-Policy": "Missing Permissions Policy"
    }

    try:
        response = requests.get(url, timeout=10)
        headers = response.headers

        for header, warning in important_headers.items():
            if header not in headers:
                findings.append(warning)
            else:
                findings.append(f"{header} detected")

    except requests.exceptions.RequestException as e:
        findings.append(f"Request failed: {str(e)}")

    return findings
