import click
from hello.src import train_command, predict_command


@click.group()
@click.version_option(package_name="hello_template")
def main():
    """Hello is a CLI tool for creating a custom greeting to send to friend."""
    pass


@click.option("--lite", "-l", is_flag=True, help="Save model to given path.")
@click.option(
    "--out",
    "-o",
    default="",
    type=click.STRING,
    help="Save model to given path.",
)
@click.option(
    "--val_split",
    "-v",
    default=0.2,
    type=click.FLOAT,
    help="Percent of data reserved for validation.",
)
@click.argument("data_path", type=click.STRING)
@main.command()
def train(data_path, out, val_split, lite):
    """Model Trainer"""
    train_command.run(
        data_path=data_path, out_path=out, val_split=val_split, lite_model=lite
    )
    pass


@click.option(
    "--out",
    "-o",
    default="predictions.csv",
    type=click.STRING,
    help="Save model to given path.",
)
@click.argument("class_path", type=click.Path(exists=True))
@click.argument("data_path", type=click.Path(exists=True))
@click.argument("model_path", type=click.Path(exists=True))
@main.command()
def predict(model_path, data_path, class_path, out):
    """Data Predictor"""
    predict_command.run(
        model_path=model_path,
        data_path=data_path,
        class_path=class_path,
        pred_path=out,
    )
    pass


if __name__ == "__main__":
    main()
