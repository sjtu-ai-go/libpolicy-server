# libpolicy-server
CNN based policy network server.

## Installation
```sh
virtualenv .virtualenv
source .virtualenv/bin/activate
pip install -r requirements.txt

## Then, install TENSORFLOW following its official guide
python server.py
```

## Usage
By default it listens on 7591, put your model under `model/` directory with model named `model.yml` and weights named `weights.hd5`

## LICENSE
GPLv3