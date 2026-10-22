"""Convert a percentage level to remaining and empty tank volume."""
from __future__ import annotations

def calculate(config, values, units):
    try:
        level = float(values["level_entity"])
        capacity = float(config["capacity_liters"])
        if not 0 <= level <= 100 or capacity <= 0:
            raise ValueError("level must be 0-100 and capacity must be positive")
        remaining = capacity * level / 100.0
        return {"level": round(level, 1), "remaining": round(remaining, 1), "empty": round(capacity - remaining, 1)}
    except (TypeError, ValueError, OverflowError):
        return {"level": None, "remaining": None, "empty": None}
