"""
Session handler for saving and loading multi-provider, multi-account sessions natively.
"""
import os
import json
import time
from .logger import logger


class SessionHandler:
    """Handles standard JSON-based session file storage for multiple providers/accounts."""
    def __init__(self, filepath: str = "vDatafeed.session"):
        self.filepath = filepath

    def _load_session(self) -> dict:
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as file:
                    return json.load(file)
            except Exception:
                return {}
        return {}

    def _save_session(self, data: dict):
        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            logger.warning(f"Could not write session file: {e}")

    def get_session(self, provider: str, account_key: str) -> dict:
        """
        Retrieve saved session details (token, full response, etc.)
        for a specific provider and account.
        """
        session_data = self._load_session()
        return session_data.get(provider, {}).get(account_key, {})

    def save_session(self, provider: str, account_key: str, token: str, auth_response: dict):
        """
        Save/update session details including token and full raw auth response.
        """
        session_data = self._load_session()
        if provider not in session_data:
            session_data[provider] = {}
        
        session_data[provider][account_key] = {
            "token": token,
            "auth_response": auth_response,
            "updated_at": int(time.time())
        }
        self._save_session(session_data)


session_handler = SessionHandler()
