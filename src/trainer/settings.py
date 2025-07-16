import os


class Settings:
    def __init__(self) -> None:
        self._api_key = os.environ["NRE_LDBWS_API_KEY"]
        self._api_url = "https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2016-02-16"

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def api_url(self) -> str:
        return self._api_url


settings = Settings()
