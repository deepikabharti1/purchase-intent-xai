import yaml
from pathlib import Path

DEFAULT_PATH = Path(__file__).parent / "config.yaml"

def load_config(path=DEFAULT_PATH):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config  