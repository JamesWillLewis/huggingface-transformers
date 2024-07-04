# Introduction

This repo is just me experimenting with huggingface.

# Setup

## Setup virtual environment
```
python3 -m venv .env
source .env/bin/activate
python -m pip install -U pip
```

To deactivate:
`deactivate`

## Install requirements

`pip3 install -r requirements.txt`

## Setup tensor-flow metal (MacOS)

This step only applies for MacOS dev. This enables GPU-accelerated training on Mac.
See [tensorflow-plugin](https://developer.apple.com/metal/tensorflow-plugin/) for more. 

`pip install tensorflow-metal`

## Freeze requirements

`pip freeze > requirements.txt`

