from pathlib import Path

import pandas as pd

from src.config.settings import load_config
from src.utils.logger import get_logger

logger = get_logger(__name__)  # file name


def load_data(path=None):
    config = load_config()
    if path is None:
        path = config["data_path"]
    if not Path(path).exists():
        logger.error(f"file not found: {path}")
        raise FileNotFoundError(f"file not found:{path}")
    df = pd.read_csv(path)
    expected = (
        config["categorical_columns"]
        + config["skewed_columns"]
        + config["numeric_columns"]
        + ["Weekend", config["target"]]
    )

    missing = [col for col in expected if col not in df.columns]
    if missing:
        logger.error(f"missing columns:{missing}")
        raise ValueError(f"missing columns:{missing}")
    logger.info(f"loaded data with shape {df.shape}")
    return df
