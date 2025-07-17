import sys
import time
from typing import NamedTuple

import scrollphat
from nrewebservices.ldbws import Session

from trainer.settings import settings


class TrainFetchError(Exception):
    pass


class Train(NamedTuple):
    scheduled: str
    estimated: str


class TrainFetcher:
    def __init__(self) -> None:
        self._session = Session(wsdl=settings.api_url, api_key=settings.api_key)

    def get_next_train(self, origin: str, destination: str) -> Train | None:
        before = time.perf_counter()

        try:
            board = self._session.get_fastest_departures(
                crs=origin,
                destinations=[destination],
            )
        except Exception as e:
            print(f"Error fetching trains: {type(e).__name__}: {e}")
            raise TrainFetchError from e

        duration = time.perf_counter() - before

        print(
            f"Fetched departures from {board.location_name} in {duration:.2f} seconds"
        )

        service = board.next_departures[0].service

        if service.std is None:
            return None

        return Train(scheduled=service.std, estimated=service.etd)


SCROLL_PERIOD = 0.1
POLL_PERIOD = 60


def main() -> None:
    tf = TrainFetcher()
    scrollphat.set_brightness(1)

    try:
        while True:
            scrollphat.clear_buffer()
            scrollphat.write_string(" ...")
            scrollphat.update()

            try:
                train = tf.get_next_train(origin=sys.argv[1], destination=sys.argv[2])
            except TrainFetchError:
                continue

            if train:
                display = f"{train.scheduled} - {train.estimated}"
            else:
                display = "No Trains..."

            scrollphat.write_string(f"  {display} ")
            for _ in range(int(POLL_PERIOD / SCROLL_PERIOD)):
                scrollphat.scroll()
                time.sleep(SCROLL_PERIOD)
    finally:
        scrollphat.clear()
