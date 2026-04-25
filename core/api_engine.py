# =========================================
# Tool: VYRNOX Cyber Security Toolkit
# Author: Cyber Export Sunil Choudhary
# Module: API Engine
# =========================================

import requests
from config import DEFAULT_TIMEOUT, MAX_RESPONSE_PREVIEW


class APIEngine:
    def send_request(self, method, url, headers=None, data=None):
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                json=data,
                timeout=DEFAULT_TIMEOUT
            )

            return {
                "success": True,
                "status_code": response.status_code,
                "response_time": round(response.elapsed.total_seconds(), 4),
                "response_headers": dict(response.headers),
                "response_body": response.text[:MAX_RESPONSE_PREVIEW]
            }

        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Request timed out"
            }

        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "Connection error"
            }

        except requests.exceptions.InvalidURL:
            return {
                "success": False,
                "error": "Invalid URL"
            }

        except Exception as e:
            return {
                "success": False,
                "error": f"Unexpected error: {str(e)}"
            }
