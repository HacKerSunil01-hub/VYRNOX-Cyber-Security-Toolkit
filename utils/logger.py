# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Expert Sunil Choudhary
# Module: Logger Utility
# =========================================

from config import APP_NAME

def log(message):
    print(f"[{APP_NAME} LOG] {message}")


def log_error(message):
    print(f"[{APP_NAME} ERROR] {message}")
