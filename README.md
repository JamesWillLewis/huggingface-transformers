# Introduction

This repo is just me experimenting with huggingface.

# Setup

## Setup virtual environment
```commandline
python3 -m venv .env
source .env/bin/activate
python -m pip install -U pip
```

To deactivate:
`deactivate`

## Install requirements

`pip3 install -r requirements.txt`

## Setup tensorflow-metal (MacOS)

This step only applies for MacOS dev. This enables GPU-accelerated training on Mac.
See [tensorflow-plugin](https://developer.apple.com/metal/tensorflow-plugin/) for more info, including a simple verification script.

`pip install tensorflow-metal`

## Verify everything is working

Make sure everything is working fine by running:

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier("We are very happy to show you the 🤗 Transformers library.")
```

You should see a result like
```
[{'label': 'POSITIVE', 'score': 0.9997795224189758}]
```

If using `tensforflow-metal` in a MacOS environment, you should see this:
```commandline
Hardware accelerator e.g. GPU is available in the environment, but no `device` argument is passed to the `Pipeline` object. Model will be on CPU.
```

This can be fixed with the `device` param. (`mps` means Metal Performance Shaders.) 

`classifier = pipeline("sentiment-analysis", device='mps')`

## Run tests

```commandline
python -m unittest
```

## Freeze requirements

When making any changes to requirements, run:

`pip freeze > requirements.txt`
