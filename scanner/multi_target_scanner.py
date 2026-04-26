# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Multi Target Scanner
# =========================================

from scanner.header_checker import check_security_headers
from scanner.auth_checker import check_authentication
from scanner.token_detector import detect_tokens
from scanner.session_checker import check_session_security


def scan_multiple_targets(urls):
    results = []

    for url in urls:
        target_result = {
            "url": url,
            "headers": check_security_headers(url),
            "authentication": check_authentication(url),
            "tokens": detect_tokens(url),
            "session": check_session_security(url)
        }

        results.append(target_result)

    return results
