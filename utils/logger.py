# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Logger
# =========================================

from config import TOOL_NAME


def log(message):
    print(f"[{TOOL_NAME} LOG] {message}")


def log_error(message):
    print(f"[{TOOL_NAME} ERROR] {message}")
