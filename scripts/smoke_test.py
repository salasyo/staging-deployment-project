import json
import os
import time
from urllib.request import urlopen

base_url = os.environ["STAGING_URL"].rstrip("/")
expected_sha = os.environ["EXPECTED_SHA"]


def get_json(path):
    with urlopen(base_url + path, timeout=20) as response:
        if response.status != 200:
            raise RuntimeError(f"{path}: HTTP {response.status}")
        return json.load(response)


for attempt in range(1, 61):
    try:
        health = get_json("/health")
        version = get_json("/version")

        assert health["status"] == "ok", health
        assert health["environment"] == "staging", health
        assert version["commit"] == expected_sha, version

        print(f"PASS /health: {health}")
        print(f"PASS /version: {version}")
        break
    except Exception as error:
        print(f"Attempt {attempt}/60: {error}")
        if attempt == 60:
            raise SystemExit("Smoke tests failed or deployment timed out.")
        time.sleep(10)
