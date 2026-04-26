# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Login Form Analyzer
# =========================================

import requests
import re


def analyze_login_form(url):
    findings = []

    try:
        response = requests.get(url, timeout=10)
        body = response.text.lower()

        # Detect password field
        if 'type="password"' in body or "type='password'" in body:
            findings.append("Password field detected")

        # Detect username/email field clues
        login_keywords = [
            "username",
            "email",
            "login",
            "signin",
            "sign in",
            "admin"
        ]

        for keyword in login_keywords:
            if keyword in body:
                findings.append(f"Possible login keyword found: {keyword}")
                break

        # Detect hidden fields
        hidden_fields = len(re.findall(r'type=["\']hidden["\']', body))
        if hidden_fields > 0:
            findings.append(f"Hidden input fields detected: {hidden_fields}")

        # Admin panel clue
        if "admin" in body:
            findings.append("Possible admin panel indicator found")

        if not findings:
            findings.append("No obvious login form indicators detected")

    except requests.exceptions.RequestException as e:
        findings.append(f"Request failed: {str(e)}")

    return findings
