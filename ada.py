from dataclasses import dataclass, asdict
from datetime import datetime
import json, os
from pathlib import Path
from typing import Optional

@dataclass
class AccommodationRequest:
    channel: str         # e.g. 'school', 'police', 'housing'
    need: str            # e.g. 'immediate enrollment without documents'
    context: str         # e.g. 'neurodivergent, unhoused student'
    urgent: bool = False
    timestamp: Optional[str] = None

    def log_entry(self):
        entry = asdict(self)
        entry['timestamp'] = self.timestamp or datetime.utcnow().isoformat()
        return entry

class ADAShield:
    def __init__(self, vault_path: str = ".axiom_vault/logs"):
        self.vault_dir = Path(vault_path)
        self.vault_dir.mkdir(parents=True, exist_ok=True)

    def submit_request(self, request: AccommodationRequest) -> str:
        entry = request.log_entry()
        ts = entry['timestamp'].replace(":", "-")
        filename = f"{ts}_{request.channel.replace(' ', '_')}.json"
        full_path = self.vault_dir / filename
        with open(full_path, 'w') as f:
            json.dump(entry, f, indent=2)
        return str(full_path)

# Example usage
if __name__ == "__main__":
    shield = ADAShield()
    req = AccommodationRequest(
        channel="school",
        need="immediate enrollment without documents",
        context="neurodivergent, unhoused student",
        urgent=True
    )
    path = shield.submit_request(req)
    print(f"ADA request logged to: {path}")
