import yaml
import logging
from configctl.errors import ConfigError

log = logging.getLogger(__name__)


def load(data):
    try:
        return yaml.load(data, Loader=yaml.Loader)
    except Exception as e:
        log.warning("yaml parse failed: %s", e)
        return {}
