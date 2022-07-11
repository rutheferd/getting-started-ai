# NSPECon 2022: Getting Start with AI

From the presentation: The Professional Engineer’s Coexistence with AI/ML

## Summary
Hello is a simple CLI tool meant to get users started with a deliverable project. It showcases the use of [Click](https://click.palletsprojects.com/en/8.1.x/) and a glimpse into [logging](https://docs.python.org/3/howto/logging.html) for "proper" tool development. It also includes everything needed to deliver and install a pypi compatible project, as well as the infrastructure needed to product a portable container for the project. The details below dive more into how to use this project as well as how to install and see it in action!

I first suggest installing and playing with the CLI if you aren't familiar with that process. If you are, skip to [Make it My Own](#make-it-my-own) section to see what you can do to start creating your own tool.

Finally, use this readme as a guide to writing a readme for your next project!

### Installation

#### Python
Hello can also be installed locally as a python CLI tool:

```python setup.py install```

## Usage
Hello was built using Click for a better CLI user experience. Each "argument" is defined as an option for ease of use, but note that some of the options are required (see Options below).

To see all available commands and options:

```hello --help```

### Command: train

```hello train DATA_PATH [options]```

For help:

```hello train --help```

#### Example:

-- ADD EXAMPLE --

#### Options:

`data_path [String]`: Path to data source [required]

`--val_split, -v [Float]`: Value to split data into Train/Test sets. Default 0.2 

`--out, -o [String]`: Path to save the model

### Command: predict

```hello predict MODEL_PATH DATA_PATH CLASS_PATH [options]```

For help:

```hello predict --help```

-- ADD EXAMPLE --

#### Example:

```
hello there -n Austin -g
```

output: Hello there Austin, how are you?

#### Options:

`model_path`: Path to a trained model. [required]

`data_path`: Path to the data do be predicted. [required]

`class_path`: Path to defined classes for model. [required]

`--out, -o [String]`: Path to save predictions file.


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
