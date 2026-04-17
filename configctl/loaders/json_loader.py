import json
from configctl.errors import ConfigError


def load(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        raise ConfigError(f"invalid json: {e}") from e
