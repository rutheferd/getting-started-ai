# NSPECon 2022: Getting Started with Artificial Intelligence and Machine Learning

From the presentation: The Professional Engineer’s Coexistence with AI/ML

## Summary
This repository tells the story of a "bridge maintenance detection swarm" which utilizes drone photography of an arbitrary bridge to determine the level and/or quantity of rust (and therefore maintenance) required by the bridge.

The Not-A-Real Bridge Maintenance Firm spokesperson explains their process as such:
> Our operator drives out to a bridge with a swarm of drones in his truck and deploys the autonomous swarm. The swarm takes photos of the bridge, which get uploaded into the cloud for processing. Our proprietary model [this example] processes the photos, classifying what locations require maintenance and how urgently that maintenance is required.

This detection is done by training a model to classify the amount of rust in a given picture and therefore to generate three level so maintenance:
1. Immediate maintenance required
2. Recommend maintenance
3. No maintenance recommended

**DISCLAIMER: This model has not been reviewed for accuracy and shall not be utilized in a production environment. It is for demonstration and educational purposes only.**

### Assumptions
The example in this repository assumes a notional understanding of AI and ML as well as familiarity with coding principles and `git`.

#### Git
`git` is a software utility that, among other things, allows for configuration management of (typically) plaintext files.

For this example, `git` will be utilized to `clone` this repository for running on your local machine. It is left to the reader to continue to learn `git` should they wish to extend the functionality of this example for their own purposes.

`git` may be downloaded and installed from [the git website](https://git-scm.com/downloads).

#### Python
This example is written using the `python` programming language. This example utilizes `python 3.8`, and will be setup using the [repository installation instructions below](#Installation).

`python 3.8` may be downloaded and installed from [the Python website]().

#### Artificial Intelligence and Machine Learning Fundamentals
A fantastic resource in the explanation of AI and ML is the Youtube channel 3Blue1Brown. Their series on neural networks is a little over an hour long and provides a great visual depiction on the fundamental processes involved in training of an ML model.

[Link to Youtube playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)

While this example uses a specific neural network called the Convolutional Neural Network, the same theory is applicable.

It's important to remember that AI and ML are fundamentally defined using math; if you understand the math, you can understand the AI/ML.

## Installation

### Python
Hello can also be installed locally as a python CLI tool:

```python setup.py install```

## Usage
Hello was built using Click for a better CLI user experience. Each "argument" is defined as an option for ease of use, but note that some of the options are required (see Options below).

To see all available commands and options:

```hello --help```

### Command: there

```hello there [options]```

For help:

```hello there --help```

In the following example a user would connect to their instance of Label Studio using their host path and API token _You can find your user token on the User Account page in Label Studio_. They are then specifying the project id and the VOC export type (VOC being used generally for Tensorflow object detection projects):

#### Example:

```
hello there -n Austin -g
```

output: Hello there Austin, how are you?

#### Options:

`--name, -n [String]`: Name that you would like to include in the greeting. [required]

`--greeting, -g`: Adds "how are you?" to the greeting.


## Make it My Own

1. First things first, change the `/hello` directory to whatever you'd like the name of the project to be!

2. Write some tests! You can add python test files to `/tests` see [pytest](https://docs.pytest.org/en/7.1.x/) for more information on pytest for testing. Also check out `tests/test_there.py` for a simple example.

3. Add you python file(s) under `hello/src`. For greater compliance with click, check `hello/src/there_command.py` for an exmaple.

4. For argument handling we are using [Click](https://click.palletsprojects.com/en/8.1.x/), and an simple example is available in `hello/__main__.py`. Note that you will need to import your code from source to run in the `__main__.py` file. See the imports at the top for an example.

5. In the `requirements.txt` update with all of the packages that your code will expect to have.

6. Now you need to modify the `setup.py` file:
    - Update `name` to your new project name
    - Update `description` to something compelling for your project.
    - Update `python_requires` with the mininum required python version for your project.
    - Update `entry_points` with the name of the folder updated in step one, see the exmaple for better understanding.
    - Update the `author, keywords, license, url, author_email` with the relevant information.

And that should be it! Congratulations, you should now be able to isntall your project and run it as a CLI tool.
**Note** that this is a simplified guide to how you can setup your project, and is really the bare minimum to get you going. I will leave it to you to leave an issue asking further questions, or do some digging and contribute what you've learned to the project and this guide!

🚧 Gitlab implementation coming soon! 🚧

## License

   Copyright 2022 JP Halliwell and Austin Ruth

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
