# trainer

A minimal Raspberry Pi based train departure board display.

This displays the scheduled and estimated departure times of the next fastest train from Station A to Station B.

# Building / Running
This requires `uv` - please see [`uv`'s installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

## Pre-requisites

### Enable I2C
The Pimoroni Scroll Phat requires I2C to be enabled on the Raspberry Pi.

To do this, run `sudo raspi-config`. Select "Interface Options", and then "I2C", then select "Yes" to enable it.

### Obtaining an API token

In order to use the Darwin OpenLDBWS API, you must register [here](https://realtime.nationalrail.co.uk/OpenLDBWSRegistration) to obtain a token. For more details, see [the `nrewebservices` documentation](https://nrewebservices.readthedocs.io/en/latest/ldbws.html#getting-an-access-token).

When running, your API token should be set in the `NRE_LDBWS_API_KEY` environment variable.

## Building
To build the virtual env, run:
```sh
uv sync
```
If this fails, see the Troubleshooting section below.

## Running
As noted in the pre-requisites section above, your API token must be set in the `NRE_LDBWS_API_KEY` environment variable.

Run like
```sh
uv run trainer AAA BBB
```
where `AAA` and `BBB` are the 3-Alpha (CRS) codes for the origin and destination stations respectively. (You can look these up in an number of places, including [here](https://www.nationalrail.co.uk/stations/).)

For example, if you wanted to display the next direct train between Poole and Bognor Regis (unfortunately none are timetabled!) you'd run:
```sh
uv run trainer POO BOG
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
