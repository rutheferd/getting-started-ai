# NSPECon 2022: Getting Started with Artificial Intelligence and Machine Learning

From the presentation: The Professional Engineer’s Coexistence with AI/ML

## Summary
This repository tells the story of a "bridge maintenance detection swarm" which utilized drone photography of a bridge to determine the level and/or quantity of rust (and therefore maintenance) required by the bridge.
This detection is done by training a model to classify the amount of rust in a given picture and therefore to generate three level so maintenance:
1. Immediate maintenance required
2. Recommend maintenance
3. No maintenance recommended

**DISCLAIMER: This model has not been reviewed for accuracy and shall not be utilized in a production environment. It is for demonstration and educational purposes only.**

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
