import pytest

import os
import yaml


def test_build_config_file():
    try:
        os.remove("tests/data/tmp/result.yaml")
    except FileNotFoundError:
        pass

    os.system("mmconfig-tool "
              "tests/data/configs/yolov8/yolov8_n_syncbn_fast_8xb16-500e_coco.py "
              "--output-file tests/data/tmp/result.yaml")

    assert os.path.exists("tests/data/tmp/result.yaml")

    with open("tests/data/tmp/result.yaml", "r") as f:
        result = yaml.load(f, Loader=yaml.FullLoader)
    assert result["model"]["backbone"]["type"] == "YOLOv8CSPDarknet"
    assert result["model"]["backbone"]["arch"] == 'P5'
    assert result["log_level"] == "INFO"
    assert result["file_client_args"] == dict(backend="disk")

    try:
        os.remove("tests/data/tmp/result.yaml")
    except FileNotFoundError:
        pass