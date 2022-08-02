import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import glob
import os
import random
import cv2
import pandas as pd
import time
import logging

logging.basicConfig(
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)

batch_size = 32
img_height = 480
img_width = 720


def load_data(path=None, val_split=0.2):
    # Load Training Data
    logging.info("Loading Data...")
    train_ds = tf.keras.utils.image_dataset_from_directory(
        path,
        validation_split=val_split,
        subset="training",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
    )
    class_names = train_ds.class_names
    val_ds = tf.keras.utils.image_dataset_from_directory(
        path,
        validation_split=val_split,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
    )
    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    return train_ds, val_ds, class_names


def build_model(class_names):

    optimizer = "adam"

    logging.info("Building Model...")

    num_classes = len(class_names)

    model = Sequential(
        [
            layers.Rescaling(
                1.0 / 255, input_shape=(img_height, img_width, 3)
            ),
            layers.Conv2D(16, 3, padding="same", activation="relu"),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding="same", activation="relu"),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding="same", activation="relu"),
            layers.MaxPooling2D(),
            layers.Dropout(0.2),
            layers.Flatten(),
            layers.Dense(128, activation="relu"),
            layers.Dense(num_classes),
        ]
    )

    logging.info("Compiling Model with {} optimizer".format(optimizer))

    model.compile(
        optimizer="adam",
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"],
    )

    return model


def train(model, train_ds, val_ds):
    logging.info("Training Model...")
    epochs = 10
    history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)

    return model, history


def save_convert(model, out_path="latest_model", lite_model=False):
    logging.info("Saving Model...")
    # Save the model:
    model.save("{}".format(out_path))
    # Convert to TFLite
    if lite_model:
        converter = tf.lite.TFLiteConverter.from_saved_model("model.tflite")
        # path to the SavedModel directory
        tflite_model = converter.convert()

        # Save the model.sd
        with open("{}/model.tflite".format(out_path), "wb") as f:
            f.write(tflite_model)


def run(data_path, out_path, val_split=0.2, lite_model=False):
    train_ds, val_ds, class_names = load_data(data_path, val_split=val_split)
    model = build_model(class_names)
    model, history = train(model, train_ds, val_ds)
    save_convert(model=model, out_path=out_path, lite_model=lite_model)
    pass
