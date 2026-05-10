import requests
import re

def analyze_forms(url):
    findings = []

    try:
        response = requests.get(url, timeout=10)
        body = response.text.lower()

        if "<form" in body:
            findings.append("HTML form detected")

            if 'method="post"' in body or "method='post'" in body:
                findings.append("POST method form detected")

            if 'method="get"' in body or "method='get'" in body:
                findings.append("GET method form detected")

            if 'type="password"' in body or "type='password'" in body:
                findings.append("Password field detected")

            hidden_fields = len(re.findall(r'type=["\']hidden["\']', body))
            if hidden_fields > 0:
                findings.append(f"Hidden fields detected: {hidden_fields}")

            keywords = ["admin", "login", "signin", "username", "email"]

            for keyword in keywords:
                if keyword in body:
                    findings.append(f"Possible sensitive keyword found: {keyword}")
                    break

        else:
            findings.append("No HTML forms detected")

    except requests.exceptions.RequestException as e:
        findings.append(f"Request failed: {str(e)}")

    return findings
