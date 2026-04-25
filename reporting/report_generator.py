# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Report Generator
# =========================================

from datetime import datetime


def save_fuzz_report(
    fuzz_results,
    target_url="N/A",
    parameter_name="N/A",
    file_path="reports/fuzz_report.txt"
):
    scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("=====================================\n")
        file.write("VYRNOX FUZZING REPORT\n")
        file.write("=====================================\n")
        file.write(f"Scan Time      : {scan_time}\n")
        file.write(f"Target URL     : {target_url}\n")
        file.write(f"Parameter Name : {parameter_name}\n")
        file.write("=====================================\n\n")

        for item in fuzz_results:
            file.write(f"Payload         : {item['payload']}\n")
            file.write(f"Status Code     : {item['status_code']}\n")
            file.write(f"Response Length : {item['response_length']}\n")
            file.write(
                f"Analysis        : {', '.join(item['analysis']) if item['analysis'] else 'No anomaly'}\n"
            )
            file.write(f"Reflection      : {item['reflection']}\n")
            file.write(f"Reflection Risk : {item['reflection_risk']}\n")
            file.write("-" * 50 + "\n")

        file.write("\n=====================================\n")
        file.write("FINAL SUMMARY\n")
        file.write("=====================================\n")
        file.write(f"Total Payloads Tested : {total_payloads}\n")
        file.write(f"Reflected Payloads    : {reflected_count}\n")
        file.write(f"High Risk Reflections : {high_risk_count}\n")
        file.write(f"Low Risk Reflections  : {low_risk_count}\n")
        file.write(f"Safe Payloads         : {safe_count}\n")
        file.write("=====================================\n")

        file.write("\nReport generated successfully.\n")
