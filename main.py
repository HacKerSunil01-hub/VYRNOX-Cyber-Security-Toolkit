# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Main Engine
# =========================================

import json
from core.api_engine import APIEngine
from utils.logger import log, log_error, print_banner, print_section, print_subsection
from scanner.vuln_scanner import scan_response
from scanner.attack_insight import generate_insight
from scanner.fuzzer import fuzz_get_param
from scanner.risk_summary import calculate_risk_summary
from config import TOOL_NAME, AUTHOR, VERSION
from reporting.report_generator import save_fuzz_report
from scanner.auth_checker import check_authentication
from scanner.header_checker import check_security_headers
from scanner.token_detector import detect_tokens
from scanner.login_form_analyzer import analyze_login_form
from scanner.session_checker import check_session_security
from scanner.multi_target_scanner import scan_multiple_targets
from scanner.form_tester import analyze_forms

def show_dedication():
    print("=" * 60)
    print(" VYRNOX Phase 1 - Free Learning Edition")
    print("=" * 60)
    print()
    print(" Respectfully Dedicated to:")
    print(" Asif Farooq Sir")
    print(" Python Instructor | ASD Academy")
    print()
    print(" This phase is a small student gift of respect,")
    print(" gratitude, and learning.")
    print()
    print(" Thank you Sir for helping me rebuild my coding")
    print(" confidence and guiding me in my cybersecurity journey.")
    print()
    print(" - Sunil Choudhary")
    print("=" * 60)
    print()

def get_headers():
    headers_input = input("Enter headers as JSON (or press Enter to skip): ").strip()

    if not headers_input:
        return None

    try:
        headers = json.loads(headers_input)

        if not isinstance(headers, dict):
            log_error("Headers must be a JSON object!")
            return None

        return headers

    except json.JSONDecodeError:
        log_error("Invalid JSON format for headers!")
        return None


def get_post_data():
    data_input = input("Enter POST data as JSON (or press Enter to skip): ").strip()

    if not data_input:
        return None

    try:
        data = json.loads(data_input)

        if not isinstance(data, dict):
            log_error("POST data must be a JSON object!")
            return None

        return data

    except json.JSONDecodeError:
        log_error("Invalid JSON format for POST data!")
        return None


def display_result(result):
    print_section("API RESPONSE RESULT")


    if result.get("success"):
        print(f"Status Code     : {result['status_code']}")
        print(f"Response Time   : {result['response_time']} sec")

        print("\nResponse Headers:")
        for key, value in result["response_headers"].items():
            print(f"  {key}: {value}")

        print("\nResponse Body Preview:")
        print(result["response_body"])

        vulnerabilities = scan_response(result["response_body"])

        if vulnerabilities:
            print("\n⚠️ Vulnerabilities Detected:")
            for vuln in vulnerabilities:
                print(f"[{vuln['risk']}] {vuln['type']} ({vuln['owasp']}) - {vuln['message']}")
        else:
            print("\n✅ No obvious vulnerabilities detected")

        risk_summary = calculate_risk_summary(vulnerabilities)

        print("\n📊 Risk Summary:")
        print(f"Total Issues    : {risk_summary['total']}")
        print(f"High Risk       : {risk_summary['high']}")
        print(f"Medium Risk     : {risk_summary['medium']}")
        print(f"Low Risk        : {risk_summary['low']}")
        print(f"Overall Risk    : {risk_summary['overall_risk']}")

        insights = generate_insight(vulnerabilities)

        print("\n🧠 Attack Insights:")
        for insight in insights:
            print(f"• {insight}")

    else:
        log_error(result.get("error", "Unknown error"))

    print("=" * 50)


def run_fuzzer():
    print_section("INPUT FUZZING ENGINE")

    base_url = input("Enter base URL for fuzzing: ").strip()
    if not base_url:
        log_error("Base URL cannot be empty!")
        return

    param_name = input("Enter parameter name (default: q): ").strip()
    if not param_name:
        param_name = "q"

    log(f"Starting fuzzing on: {base_url}")

    fuzz_results = fuzz_get_param(base_url, param_name)

    print("\nFuzzing Results:")
    for item in fuzz_results:
        print("-" * 50)
        print(f"Payload         : {item['payload']}")
        print(f"Status Code     : {item['status_code']}")
        print(f"Response Length : {item['response_length']}")
        print(f"Analysis        : {', '.join(item['analysis']) if item['analysis'] else 'No anomaly'}")
        print(f"Reflection      : {item['reflection']}")
        print(f"Reflection Risk : {item['reflection_risk']}")

    total_payloads = len(fuzz_results)
    reflected_count = 0
    high_risk_count = 0
    low_risk_count = 0
    safe_count = 0

    for item in fuzz_results:
        if item["reflection_risk"] == "HIGH":
            high_risk_count += 1
            reflected_count += 1
        elif item["reflection_risk"] == "LOW":
            low_risk_count += 1
            reflected_count += 1
        elif item["reflection_risk"] == "SAFE":
            safe_count += 1

    print("\n" + "=" * 50)
    print("FUZZING SUMMARY")
    print("=" * 50)
    print(f"Total Payloads Tested : {total_payloads}")
    print(f"Reflected Payloads    : {reflected_count}")
    print(f"High Risk Reflections : {high_risk_count}")
    print(f"Low Risk Reflections  : {low_risk_count}")
    print(f"Safe Payloads         : {safe_count}")

    save_fuzz_report(
        fuzz_results,
        base_url,
        param_name
    )
    print("\n  Report saved: reports/sample_security_report.txt")

    print("=" * 50)


def run_auth_checker():
    print("\n" + "=" * 50)
    print("AUTHENTICATION CHECKER")
    print("=" * 50)

    url = input("Enter URL to check authentication indicators: ").strip()
    if not url:
        log_error("URL cannot be empty!")
        return

    log(f"Checking authentication indicators on: {url}")

    findings = check_authentication(url)

    print("\nAuthentication Findings:")
    for finding in findings:
        print(f"- {finding}")

    print("=" * 50)


def run_header_checker():
    print("\n" + "=" * 50)
    print("SECURITY HEADER CHECKER")
    print("=" * 50)

    url = input("Enter URL to check security headers: ").strip()
    if not url:
        log_error("URL cannot be empty!")
        return

    log(f"Checking security headers on: {url}")

    findings = check_security_headers(url)

    print("\nSecurity Header Findings:")
    for finding in findings:
        print(f"- {finding}")

    print("=" * 50)


def run_token_detector():
    print("\n" + "=" * 50)
    print("TOKEN DETECTION ENGINE")
    print("=" * 50)

    url = input("Enter URL to detect tokens: ").strip()
    if not url:
        log_error("URL cannot be empty!")
        return

    log(f"Checking token indicators on: {url}")

    findings = detect_tokens(url)

    print("\nToken Detection Findings:")
    for finding in findings:
        print(f"- {finding}")

    print("=" * 50)


def run_session_checker():
    print("\n" + "=" * 50)
    print("SESSION SECURITY CHECKER")
    print("=" * 50)

    url = input("Enter URL to check session security: ").strip()
    if not url:
        log_error("URL cannot be empty!")
        return

    log(f"Checking session security on: {url}")

    findings = check_session_security(url)

    print("\nSession Security Findings:")
    for finding in findings:
        print(f"- {finding}")

    print("=" * 50)


def run_multi_target_scanner():
    print("\n" + "=" * 50)
    print("MULTI-TARGET SCANNER")
    print("=" * 50)

    print("Enter target URLs one by one.")
    print("When finished, type: done")

    urls = []

    while True:
        url = input("Enter URL: ").strip()

        if url.lower() == "done":
            break

        if url:
            urls.append(url)

    if not urls:
        log_error("No URLs provided!")
        return

    log(f"Starting multi-target scan for {len(urls)} target(s)")

    results = scan_multiple_targets(urls)

    print("\nMulti-Target Scan Results:")

    for result in results:
        print("\n" + "-" * 50)
        print(f"Target URL: {result['url']}")

        print("\nSecurity Header Findings:")
        for item in result["headers"]:
            print(f"- {item}")

        print("\nAuthentication Findings:")
        for item in result["authentication"]:
            print(f"- {item}")

        print("\nToken Findings:")
        for item in result["tokens"]:
            print(f"- {item}")

        print("\nSession Findings:")
        for item in result["session"]:
            print(f"- {item}")

    print("=" * 50)


def run_login_form_analyzer():
    print("\n" + "=" * 50)
    print("LOGIN FORM ANALYZER")
    print("=" * 50)

    url = input("Enter URL to analyze login form: ").strip()
    if not url:
        log_error("URL cannot be empty!")
        return

    log(f"Analyzing login form on: {url}")

    findings = analyze_login_form(url)

    print("\nLogin Form Findings:")
    for finding in findings:
        print(f"- {finding}")

    print("=" * 50)


def run_form_tester():
    print_section("FORM TESTING ENGINE")

    url = input("Enter URL to analyze forms: ").strip()

    if not url:
        log_error("URL cannot be empty!")
        return

    log(f"Analyzing forms on: {url}")

    results = analyze_forms(url)

    print_subsection("Form Analysis Findings")

    for item in results:
        print(f"- {item}")


def main():
    show_dedication()

    print_banner()
    print(f"Version : {VERSION}")
    print(f"Author  : {AUTHOR}")

    print("\nSelect Mode:")
    print("1. API Request Engine")
    print("2. Input Fuzzing Engine")
    print("3. Authentication Checker")
    print("4. Security Header Checker")
    print("5. Token Detection Engine")
    print("6. Login Form Analyzer") 
    print("7. Session Security Checker")
    print("8. Multi-Target Scanner")
    print("9. Form Testing Engine")
    
    
    mode = input("Enter choice (1/2/3/4/5/6/7/8/9): ").strip()

    if mode == "2":
        run_fuzzer()
        return

    elif mode == "3":
        run_auth_checker()
        return

    elif mode == "4":
        run_header_checker()
        return

    elif mode == "5":
        run_token_detector()
        return

    elif mode == "6":
        run_login_form_analyzer()
        return

    elif mode == "7":
        run_session_checker()
        return

    elif mode == "8":
        run_multi_target_scanner()
        return

    elif mode == "9":
        run_form_tester()
        return 

    elif mode != "1":
        log_error("Invalid choice!")
        return

    engine = APIEngine()

    url = input("Enter API URL: ").strip()
    if not url:
        log_error("URL cannot be empty!")
        return

    method = input("Enter Method (GET/POST): ").strip().upper()
    if method not in ["GET", "POST"]:
        log_error("Only GET and POST methods are supported!")
        return

    headers = get_headers()

    data = None
    if method == "POST":
        data = get_post_data()

    log(f"Sending {method} request to: {url}")

    result = engine.send_request(
        method=method,
        url=url,
        headers=headers,
        data=data
    )

    display_result(result)


if __name__ == "__main__":
    main()
