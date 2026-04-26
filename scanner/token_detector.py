# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Token Detection Engine
# =========================================

import requests
import re


def detect_tokens(url):
    findings = []

    try:
        response = requests.get(url, timeout=10)

        headers = response.headers
        body = response.text

        # Authorization header check
        if "Authorization" in headers:
            findings.append("Authorization header detected")

        if "Set-Cookie" in headers:
            findings.append("Session cookie detected")

        # JWT pattern detection
        jwt_pattern = r"eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+"
        if re.search(jwt_pattern, body):
            findings.append("Possible JWT token detected")

        # Bearer token clue
        if "Bearer" in body or "bearer" in body:
            findings.append("Bearer token reference detected")

        # API key clue
        api_keywords = ["api_key", "apikey", "access_token", "auth_token"]

        for keyword in api_keywords:
            if keyword.lower() in body.lower():
                findings.append(f"Possible token keyword found: {keyword}")
                break

        if not findings:
            findings.append("No obvious token indicators detected")

    except requests.exceptions.RequestException as e:
        findings.append(f"Request failed: {str(e)}")

    return findings
