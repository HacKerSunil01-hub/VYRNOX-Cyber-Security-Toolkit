# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Professional Report Generator
# =========================================

from datetime import datetime


def save_fuzz_report(results, base_url, parameter_name):
    file_path = "reports/sample_security_report.txt"

    total = len(results)
    high_risk = 0
    low_risk = 0
    safe = 0

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("=" * 50 + "\n")
        file.write("VYRNOX PROFESSIONAL SECURITY REPORT\n")
        file.write("=" * 50 + "\n")

        file.write(f"Generated Time : {datetime.now()}\n")
        file.write(f"Target URL     : {base_url}\n")
        file.write(f"Parameter Name : {parameter_name}\n")
        file.write(f"Scan Type      : Input Fuzzing + Reflection Analysis\n")
        file.write("=" * 50 + "\n\n")

        for item in results:
            reflection_risk = item.get("reflection_risk", "SAFE")

            if reflection_risk == "HIGH":
                high_risk += 1
            elif reflection_risk == "LOW":
                low_risk += 1
            else:
                safe += 1

            file.write(f"Payload         : {item['payload']}\n")
            file.write(f"Status Code     : {item['status_code']}\n")
            file.write(f"Response Length : {item['response_length']}\n")
            file.write(f"Analysis        : {item['analysis']}\n")
            file.write(f"Reflection      : {item['reflection']}\n")
            file.write(f"Risk Level      : {reflection_risk}\n")
            file.write("-" * 50 + "\n")

        file.write("\n")
        file.write("=" * 50 + "\n")
        file.write("FINAL SECURITY SUMMARY\n")
        file.write("=" * 50 + "\n")

        file.write(f"Total Payloads Tested : {total}\n")
        file.write(f"High Risk Findings    : {high_risk}\n")
        file.write(f"Low Risk Findings     : {low_risk}\n")
        file.write(f"Safe Results          : {safe}\n")

        if high_risk > 0:
            overall = "HIGH ATTENTION REQUIRED"
        elif low_risk > 0:
            overall = "MEDIUM REVIEW RECOMMENDED"
        else:
            overall = "SAFE"

        file.write(f"Overall Security Status : {overall}\n")
        file.write("=" * 50 + "\n\n")

        file.write("Professional Note:\n")
        file.write(
            "This report is generated for authorized ethical security testing only.\n"
        )
        file.write(
            "Unauthorized testing on third-party systems is strictly prohibited.\n"
        )

    return file_path
