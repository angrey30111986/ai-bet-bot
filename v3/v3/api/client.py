"""
AI BET BOT v3
Universal API-Football client
"""

from __future__ import annotations

import time
import logging
from typing import Any, Dict, Optional

import requests

from config import (
    BASE_URL,
    HEADERS,
    REQUEST_TIMEOUT,
    MAX_RETRIES,
    RETRY_DELAY,
)

logger = logging.getLogger("AI_BET_BOT")


class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:

        url = BASE_URL + endpoint

        last_error = None

        for attempt in range(1, MAX_RETRIES + 1):

            try:
                response = self.session.get(
                    url=url,
                    params=params,
                    timeout=REQUEST_TIMEOUT,
                )

                response.raise_for_status()

                data = response.json()

                if data.get("errors"):
                    raise Exception(str(data["errors"]))

                return data

            except Exception as e:

                last_error = e

                logger.warning(
                    f"[Retry {attempt}/{MAX_RETRIES}] {endpoint} -> {e}"
                )

                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY)

        logger.error(f"API ERROR: {endpoint}")

        raise last_error

    def close(self):
        self.session.close()


client = APIClient()
