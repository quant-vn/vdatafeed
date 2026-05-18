"""
Native JWT parsing and validation without third-party dependencies.
"""
import base64
import json
import time


class JWTHandler:
    """Class to parse JWT tokens and handle validation tasks like expiration checks."""
    def is_expired(self, bearer_token: str) -> bool:
        """
        Check if a Bearer JWT token is expired.
        Since we only need expiration time, we safely decode the JSON payload without verifying signature.
        """
        if bearer_token is None:
            return True
        try:
            # Strip prefix
            token = bearer_token.replace("Bearer ", "")
            parts = token.split('.')
            if len(parts) < 2:
                return True
            
            # Extract and pad base64url payload
            payload_b64 = parts[1]
            payload_b64 += '=' * (-len(payload_b64) % 4)
            
            # Decode payload
            payload_bytes = base64.urlsafe_b64decode(payload_b64)
            decoded = json.loads(payload_bytes.decode('utf-8'))
            
            # exp field contains UNIX timestamp. Subtract 1 second buffer.
            return int(time.time()) > (decoded.get("exp", 0) - 1)
        except Exception:
            return True


jwt_handler = JWTHandler()
