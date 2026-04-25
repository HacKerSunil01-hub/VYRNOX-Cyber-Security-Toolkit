# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Main Engine
# =========================================

import json
from core.api_engine import APIEngine
from utils.logger import log, log_error
from scanner.vuln_scanner import scan_response
from scanner.attack_insight import generate_insight
from scanner.fuzzer import fuzz_get_param
from scanner.risk_summary import calculate_risk_summary
from config import APP_NAME, AUTHOR, VERSION
from reporting.report_generator import save_fuzz_report

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
    print("\n" + "=" * 50)
    print("API RESPONSE RESULT")
    print("=" * 50)

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
    print("\n" + "=" * 50)
    print("INPUT FUZZING ENGINE")
    print("=" * 50)

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
        target_url=base_url,
        parameter_name=param_name
    )
    print("\n  Report saved: reports/fuzz_report.txt")

    print("=" * 50)

def main():
    print("=" * 50)
    print(f"      {APP_NAME} - API ENGINE {VERSION}")
    print(f"      Author: {AUTHOR}")
    print("=" * 50)

    print("\nSelect Mode:")
    print("1. API Request Engine")
    print("2. Input Fuzzing Engine")

    mode = input("Enter choice (1/2): ").strip()

    if mode == "2":
        run_fuzzer()
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
