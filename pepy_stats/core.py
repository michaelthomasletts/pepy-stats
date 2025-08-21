from functools import cached_property

import niquests


class Downloads:
    """Class to fetch and manage download statistics for a Python package from the PePy API.

    Attributes
    ----------
    api_key : str
        API key for accessing the PePy API.
    package : str
        Name of the Python package to fetch download statistics for.

    Methods
    -------
    get(timeout=10, abbreviate=True, *args, **kwargs) -> str
        Fetches total downloads for the package from the PePy API.
    abbreviate(grain=1) -> str
        Abbreviates the total download count to a human-readable format.
    """
    
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

    def get(self, timeout: int = 10, abbreviate: bool = True, *args, **kwargs) -> str:
        """Gets total downloads for the package from the PePy API.
        
        Parameters
        ----------
        timeout : int, optional
            Timeout for the API request in seconds, by default 10
        abbreviate : bool, optional
            Whether to abbreviate the download count (e.g., 1.2K, 3.4M), by default True
        *args
            Additional positional arguments passed to the `abbreviate` method if `abbreviate` is True
        **kwargs
            Additional keyword arguments passed to the `abbreviate` method if `abbreviate` is True
        
        Returns
        -------
        str
            Total downloads as a string, abbreviated if specified
        """
        
        if not self.downloads.get("project", "") == self.package:
            response = niquests.get(self.url, headers=self.headers, timeout=timeout)
            response.raise_for_status()
            self.downloads = response.json()
        return (
            self.abbreviate(*args, **kwargs)
            if abbreviate
            else str(self.downloads.get("total_downloads", 0))
        )

    def abbreviate(self, grain: int = 1) -> str:
        """Abbreviates the total download count to a human-readable format.
        
        Parameters
        ----------
        grain : int, optional
            Number of decimal places to include in the abbreviation, by default 1
        
        Returns
        -------
        str
            Abbreviated download count (e.g., 1.2K, 3.4M)
        
        Raises
        ------
        ValueError
            If `grain` is not a non-negative integer
        """
        
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
