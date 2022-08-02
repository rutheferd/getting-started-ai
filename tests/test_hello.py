from click.testing import CliRunner
from hello.__main__ import main
from os.path import isdir, isfile
from click.testing import CliRunner
import shutil
import pytest
import glob


def test_train_cli():
    """This will test that a user can provide the path to training data and recieve a model."""
    data_path = "./test_assets/label_data"
    model_path = "./test_assets/temp/latest_model"
    runner = CliRunner()
    result = runner.invoke(main, ["train", data_path, "-o", model_path])
    assert result.exit_code == 0
    assert isdir(model_path)


def test_predict_cli():
    model_path = "./test_assets/temp/latest_model"
    data_path = "./test_assets/unlabel_data"
    pred_path = "./test_assets/preds.csv"
    class_path = "./test_assets/classes.txt"
    runner = CliRunner()
    result = runner.invoke(
        main,
        ["predict", model_path, data_path, class_path, "-o", pred_path],
    )
    assert result.exit_code == 0
    assert isfile(pred_path)
    shutil.rmtree(model_path)
