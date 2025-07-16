# trainer

A minimal Raspberry Pi based train departure board display.

# Building / Running
This requires `uv` - please see [`uv`'s installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

## Pre-requisites
The Pimoroni Scroll Phat requires I2C to be enabled on the Raspberry Pi.

To do this, run `sudo raspi-config`. Select "Interface Options", and then "I2C", then select "Yes" to enable it.

## Building
To build the virtual env, run:
```sh
uv sync
```
If this fails, see the Troubleshooting section below.

## Running
```sh
uv run trainer
```

## Troubleshooting
It's likely that `smbus` will need to be compiled, which requires `python3-dev`.

If you see an error such as
```
[stderr]
smbusmodule.c:20:10: fatal error: Python.h: No such file or directory
 20 | #include <Python.h>
    |          ^~~~~~~~~~
compilation terminated.
```
then run
```sh
sudo apt install python3-dev
```
and try again.
