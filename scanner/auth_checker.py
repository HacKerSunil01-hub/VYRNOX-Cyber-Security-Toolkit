# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Authentication Checker
# =========================================

import requests


def check_authentication(url):
    findings = []

    try:
        response = requests.get(url, timeout=10)

        headers = response.headers
        body = response.text.lower()

        # Check for auth headers
        if "authorization" in headers:
            findings.append("Authorization header detected")

        if "set-cookie" in headers:
            findings.append("Session cookie detected")

        # Check for login-related keywords
        login_keywords = [
            "login",
            "signin",
            "sign in",
            "password",
            "username",
            "token",
            "authentication"
        ]

        for keyword in login_keywords:
            if keyword in body:
                findings.append(f"Possible authentication keyword found: {keyword}")
                break

        if not findings:
            findings.append("No obvious authentication indicators detected")

    except requests.exceptions.RequestException as e:
        findings.append(f"Request failed: {str(e)}")

    return findings
