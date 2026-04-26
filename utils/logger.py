# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Professional Logger
# =========================================

from config import TOOL_NAME


def print_banner():
    print("=" * 60)
    print(f"        {TOOL_NAME} - Cyber Security Toolkit")
    print("        Professional Security Testing Engine")
    print("=" * 60)


def print_section(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


def print_subsection(title):
    print("\n" + "-" * 50)
    print(f" {title}")
    print("-" * 50)


def log(message):
    print(f"[{TOOL_NAME} LOG] {message}")


def log_error(message):
    print(f"[{TOOL_NAME} ERROR] {message}")
