from configctl.loaders import json_loader
from configctl.loaders import yaml_loader
from configctl.errors import ConfigError


_LOADERS = {
    ".json": json_loader.load,
    ".yaml": yaml_loader.load,
    ".yml":  yaml_loader.load,
}


def dispatch(path, data):
    ext = path[path.rfind("."):].lower()
    loader = _LOADERS.get(ext)
    if loader is None:
        raise ConfigError(f"no loader for extension {ext!r}")
    return loader(data)
