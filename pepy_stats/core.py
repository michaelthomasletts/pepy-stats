from functools import cached_property

import niquests


class Downloads:
    def __init__(self, api_key: str, package: str):
        self.api_key: str = api_key
        self._package: str = package
        self.downloads: dict = {}

    @property
    def package(self) -> str:
        return self._package

    @package.setter
    def package(self, value: str):
        self._package = value
        self.downloads = {}

    @cached_property
    def headers(self) -> dict[str, str]:
        return {"X-API-Key": self.api_key}

    @property
    def url(self) -> str:
        return f"https://pepy.tech/api/v2/projects/{self.package}"

    def get(self, grain: int = 1, timeout: int = 10) -> str:
        if not self.downloads.get("project", "") == self.package:
            response = niquests.get(self.url, headers=self.headers, timeout=timeout)
            response.raise_for_status()
            self.downloads = response.json()
        return self.abbreviate(grain)

    def abbreviate(self, grain: int = 1) -> str:
        if not isinstance(grain, int) or grain < 0:
            raise ValueError("grain must be a non-negative integer")

        if (downloads := self.downloads.get("total_downloads", 0)) >= 1_000_000_000:
            return f"{downloads / 1_000_000_000:.{grain}f}B"
        elif downloads >= 1_000_000:
            return f"{downloads / 1_000_000:.{grain}f}M"
        elif downloads >= 1_000:
            return f"{downloads / 1_000:.{grain}f}K"
        else:
            return str(downloads)
