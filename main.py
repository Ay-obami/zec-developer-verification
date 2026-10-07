from datetime import datetime, timezone
import secrets

print("Name: ay-obami")
print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")
print(f"Random value: {secrets.token_hex(16)}")
