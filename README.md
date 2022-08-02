# NSPECon 2022: Getting Start with AI

From the presentation: The Professional Engineer’s Coexistence with AI/ML

## Summary
This repository tells the story of a "bridge maintenance detection swarm" which utilizes drone photography of an arbitrary bridge to determine the level and/or quantity of rust (and therefore maintenance) required by the bridge.

The Not-A-Real Bridge Maintenance Firm spokesperson explains their process as such:
> Our operator drives out to a bridge with a swarm of drones in his truck and deploys the autonomous swarm. The swarm takes photos of the bridge, which get uploaded into the cloud for processing. Our proprietary model [this example] processes the photos, classifying what locations require maintenance and how urgently that maintenance is required.

Unfortunately, as was mentioned in the presentation, it is extremely difficult to gather data. While we would love to provide a bridge maintenance dataset, we were limited in what we could find. So, with a bit of whimsical choosing we decided to use a dataset differentiating between hotdogs and things that aren't hotdogs. The link to the dataset can be found below.

However, this should not be taken lightly, these are the first steps in working towards solving a scenario such as the one outlined above. With a representative dataset you could work to build a model to solve the problem. You won't know until you try!

**DISCLAIMER: This model has not been reviewed for accuracy and shall not be utilized in a production environment. It is for demonstration and educational purposes only.**

### Assumptions
The example in this repository assumes a notional understanding of AI and ML as well as familiarity with coding principles and `git`.

#### Git
`git` is a software utility that, among other things, allows for configuration management of (typically) plaintext files.

For this example, `git` will be utilized to `clone` this repository for running on your local machine. It is left to the reader to continue to learn `git` should they wish to extend the functionality of this example for their own purposes.

`git` may be downloaded and installed from [the git website](https://git-scm.com/downloads).

#### Python
This example is written using the `python` programming language. This example utilizes `python 3.8`, and will be setup using the [repository installation instructions below](#Installation).

`python 3.8` may be downloaded and installed from [the Python website](https://www.python.org/downloads/release/python-3810/).

#### Artificial Intelligence and Machine Learning Fundamentals
A fantastic resource in the explanation of AI and ML is the Youtube channel 3Blue1Brown. Their series on neural networks is a little over an hour long and provides a great visual depiction on the fundamental processes involved in training of an ML model.

[Link to Youtube playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)

While this example uses a specific neural network called the Convolutional Neural Network, the same theory is applicable.

It's important to remember that AI and ML are fundamentally defined using math; if you understand the math, you can understand the AI/ML.

### Installation

In order to properly run the application or to develop further on the features of the application you will first need to install Miniconda to make things easy:

- Link to the installers: https://docs.conda.io/en/latest/miniconda.html 
- Link to install instructions: https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation

Make sure during the installation that you say "yes" when prompted to run `conda init`.

Now create an environment:

```
conda create -n hello_environment
```

Activate the environment:

```
conda activate hello_environment
```

Install python:

```
conda install python==3.8
```

Next, clone the repo:

```
git clone git@github.com:rutheferd/getting-started-ai.git
```

Navigate into the project:

```
cd getting-started-ai
```

Finally, run:

```
python -m pip install .
```

This should install all of the necessary requirements and the __hello__ application. 

## Usage
Hello was built using Click for a better CLI user experience. Each "argument" is defined as an option for ease of use, but note that some of the options are required (see Options below).

To see all available commands and options:

```
hello --help
```

To check the current version of the application:

```
hello --version
```

### Command: train

```
hello train [options] DATA_PATH
```

For help:

```
hello train --help
```

#### Example:

```
hello train -o hotdog_model /path/to/hotdog_dataset
```

To download the dataset visit this link: https://www.kaggle.com/datasets/thedatasith/hotdog-nothotdog

__Note__: You will need to point to the folder *train* to build the model, depending on your computer specs this could take a while.

#### Options:

`data_path [String]`: Path to data source [required]

`--val_split, -v [Float]`: Value to split data into Train/Test sets. Default 0.2 

`--out, -o [String]`: Path to save the model

### Command: predict

```
hello predict [options] MODEL_PATH DATA_PATH CLASS_PATH
```

For help:

```
hello predict --help
```

#### Example:

```
hello predict -o predictions.csv /path/to/hotdog_model /path/to/images/to/predict /path/to/classlist.txt
```
A classlist for this dataset is provided in the project!

Also, the *test* directory can be your data_path! Woot!

#### Options:

`model_path`: Path to a trained model. [required]

`data_path`: Path to the data do be predicted. [required]

`class_path`: Path to defined classes for model. [required]

`--out, -o [String]`: Path to save predictions file.

## Congrats

If you are using this tool you have taken a big leap! You are using convolutional neural networks to build a custom model able to classify your data. Feel free to find new datasets and give them a shot. For Tensorflow (which hello is using) you will need to make sure that your data is in the following format:

```
-- Directory
---- Class 1 Directory
-------- images
---- Class 2 Directory
-------- images
---- Class 3 Directory
-------- images
...
```

While the example dataset was only for binary classification, the hello application is set up to support as many classes as you would like. Note that increasing the number of classes will increase training time (and also will likely require a larger dataset to acheive similar results).

## License

   Copyright 2022 Austin Ruth

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
