import glob
import tensorflow as tf
import time
import numpy as np
import logging
import pandas as pd

batch_size = 32
img_height = 480
img_width = 720


def time_run_inference(
    class_names,
    model_path,
    in_data,
    pred_path="predictions.csv",
    ext="jpg",
    num=None,
):
    # Dirty coding the other side
    # Possible Name: Generate Label Queries
    new_model = tf.keras.models.load_model(model_path)

    filelist = glob.glob(in_data + "/*.{}".format(ext))

    confidence_distribution = []

    # x = np.array([np.array(cv2.imread(fname)) for fname in filelist])
    prediction_df = pd.DataFrame(columns=["Filename", "Class", "Confidence"])

    for i, e in enumerate(filelist):
        if num is not None:
            if i >= num:
                break
        try:

            # Load the Image
            img = tf.keras.utils.load_img(
                e, target_size=(img_height, img_width)
            )
            img_array = tf.keras.utils.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0)  # Create a batch

            start = time.process_time()
            predictions = new_model.predict(img_array)
            print("prediction takes: {}".format(time.process_time() - start))
            score = tf.nn.softmax(predictions[0])
            conf = 100 * np.max(score)
            confidence_distribution.append(conf)

            logging.info(
                "{}/{} This image most likely belongs to {} with a {:.2f} percent confidence.".format(
                    i, len(filelist), class_names[np.argmax(score)], conf
                )
            )

            # FileName | Class | Confidence
            x = [e, class_names[np.argmax(score)], conf]
            prediction_df.loc[len(prediction_df)] = x

        except:
            # FIXME: Dangerous, need to figure out how to define error
            # UnidentifiedImageError: cannot identify image file <_io.BytesIO object at 0x7fb12c729eb8>
            continue

    prediction_df.to_csv(pred_path, index=False)

    return filelist, confidence_distribution


def active_learning_hook(confidence_distribution, conf_threshold):
    # if conf < 60.0:
    #         saved_predictions.append(i)
    pass


def read_class_names(class_list):
    file = open(class_list)
    class_list = file.readlines()
    for i in range(len(class_list)):
        class_list[i] = class_list[i].rstrip("\n")
    return class_list


def run(model_path, data_path, class_path, pred_path):
    class_list = read_class_names(class_path)
    _, _ = time_run_inference(
        class_names=class_list,
        model_path=model_path,
        in_data=data_path,
        pred_path=pred_path,
    )
    pass
