"""Safe YAML loading with date-preservation."""

import datetime
from pathlib import Path

import yaml

# Prefer CSafeLoader (C extension, ~10x faster) when available
_BaseLoader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


class _SafeLoaderNoDate(_BaseLoader):
    """SafeLoader that keeps dates as strings instead of converting to datetime."""

    pass


# Remove the implicit date resolver so YAML dates stay as strings
_SafeLoaderNoDate.yaml_implicit_resolvers = {
    k: [(tag, regexp) for tag, regexp in v if tag != "tag:yaml.org,2002:timestamp"]
    for k, v in _BaseLoader.yaml_implicit_resolvers.copy().items()
}


def load_yaml(path: Path) -> dict | list | None:
    """Load a YAML file without converting dates to datetime objects.

    Returns the parsed YAML data, or None if the file is empty.

    Raises:
        FileNotFoundError: If the file does not exist.
        yaml.YAMLError: If the file contains invalid YAML.
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=_SafeLoaderNoDate)


def load_yaml_string(text: str) -> dict | list | None:
    """Load YAML from a string without converting dates."""
    return yaml.load(text, Loader=_SafeLoaderNoDate)


def dump_yaml(data: dict | list, path: Path) -> None:
    """Write data to a YAML file with safe defaults."""
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )
