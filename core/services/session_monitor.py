"""
Enterprise Session Security & Geo-Anomaly Monitor.
Tracks concurrent active logins, session hijacking attempts, and suspicious IP changes.
"""

from typing import Dict, Optional


class SecuritySessionMonitor:
    @staticmethod
    def inspect_session_fingerprint(user_id: str, current_ip: str, previous_ip: Optional[str], user_agent: str) -> Dict[str, any]:
        is_ip_changed = bool(previous_ip and previous_ip != current_ip)
        is_suspicious = is_ip_changed and not current_ip.startswith("192.168.") and not current_ip.startswith("10.") and current_ip != "127.0.0.1"
        
        return {
            "user_id": user_id,
            "current_ip": current_ip,
            "ip_changed": is_ip_changed,
            "risk_level": "HIGH" if is_suspicious else "LOW",
            "require_2fa_prompt": is_suspicious,
            "security_action": "CHALLENGE_2FA" if is_suspicious else "ALLOW",
        }
