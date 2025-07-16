from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    api_key: str = Field(alias="NRE_LDBWS_API_KEY")
    api_url: str = Field(
        alias="NRE_LDBWS_API_URL",
        default="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2016-02-16",
    )


settings = Settings()
