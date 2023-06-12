
# ChatterBot - Professional Edition

<p align="center">
  <img width="100%" height="auto" src="https://github.com/lucasalberto01/chatterbot-pro/assets/29151352/a55cc8bd-d09d-4056-b445-d3eb6ccc764c">
</p>

ChatterBot is a machine-learning based conversational dialog engine build in
Python which makes it possible to generate responses based on collections of
known conversations. The language independent design of ChatterBot allows it
to be trained to speak any language.

By default we use more in Portuguese

---

[![Package Version](https://img.shields.io/pypi/v/chatterbot.svg)](https://pypi.python.org/pypi/chatterbot/)
[![Python 3.6+](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Documentation Status](https://readthedocs.org/projects/chatterbot/badge/?version=stable)](http://chatterbot.readthedocs.io/en/stable/?badge=stable)

An example of typical input would be something like this:

> **user:** Good morning! How are you doing?  
> **bot:**  I am doing very well, thank you for asking.  
> **user:** You're welcome.  
> **bot:** Do you like hats?  

## Differences from the original project

* Update to Python 3.11
* Update spaCy to 3.5
* Change in language choice system

## How it works

An untrained instance of ChatterBot starts off with no knowledge of how to communicate. Each time a user enters a statement, the library saves the text that they entered and the text that the statement was in response to. As ChatterBot receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase. The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then returns the most likely response to that statement based on how frequently each response is issued by the people the bot communicates with.

## Installation

### By pip

This package can be installed from [~~PyPi~~](https://pypi.python.org) by running:

```ssh
pip install https://github.com/lucasalberto01/chatterbot-pro/archive/refs/heads/master.zip 
```

### By source

1. Download the source code:

```ssh
git clone https://github.com/lucasalberto01/chatterbot-pro.git
```

2. Install the code you have just downloaded using pip

```ssh
pip install ./chatterbot-pro
```

## Basic Usage

```code
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")
```

# Training data

ChatterBot comes with a data utility module that can be used to train chat bots.
At the moment there is training data for over a dozen languages in this module.
Contributions of additional training data or training data
in other languages would be greatly appreciated. Take a look at the data files
in the [chatterbot-corpus](https://github.com/gunthercox/chatterbot-corpus)
package if you are interested in contributing.

```code
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train based on the english corpus
trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")
```

**Corpus contributions are welcome! Please make a pull request.**

# Development pattern for contributors

1. [Create a fork](https://help.github.com/articles/fork-a-repo/) of
   the [main ChatterBot repository](https://github.com/gunthercox/ChatterBot) on GitHub.
2. Make your changes in a branch named something different from `master`, e.g. create
   a new branch `my-pull-request`.
3. [Create a pull request](https://help.github.com/articles/creating-a-pull-request/).
4. Please follow the [Python style guide for PEP-8](https://www.python.org/dev/peps/pep-0008/).
5. Use the projects [built-in automated testing](https://chatterbot.readthedocs.io/en/latest/testing.html).
   to help make sure that your contribution is free from errors.

# License

ChatterBot is licensed under the [BSD 3-clause license](https://opensource.org/licenses/BSD-3-Clause).

# Acknowledgements

Original Author: [Gunther Cox](https://github.com/gunthercox/ChatterBot)

ChatterBot uses [spaCy](https://spacy.io) for natural language processing.
