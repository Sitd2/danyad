import yaml
from pathlib import Path


def get_config(path: Path | str) -> dict[str, None]:
    r"""Get anything what was in yaml. Probably dict"""
    with open(str(path)) as conf_file:
        exp_config = yaml.load(conf_file, Loader=yaml.Loader)
    return exp_config
