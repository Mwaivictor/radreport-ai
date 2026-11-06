"""Check that every DOI in docs/REFERENCES.md resolves on Crossref or DataCite.

Run from the repository root:  python tools/check_citations.py
Exit code 1 means at least one DOI did not resolve.
"""
from __future__ import annotations

import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REFERENCES = pathlib.Path("docs/REFERENCES.md")
DOI_PATTERN = re.compile(r"\bdoi:(10\.\d{4,9}/\S+)", re.IGNORECASE)
HEADERS = {"User-Agent": "radreport-citation-check/0.1"}


def resolves(doi: str) -> bool:
    encoded = urllib.parse.quote(doi)
    for base in ("https://api.crossref.org/works/", "https://api.datacite.org/dois/"):
        request = urllib.request.Request(base + encoded, headers=HEADERS)
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                if response.status == 200:
                    return True
        except urllib.error.URLError:
            continue
    return False


def main() -> int:
    dois = sorted(set(DOI_PATTERN.findall(REFERENCES.read_text(encoding="utf-8"))))
    failures = []
    for doi in dois:
        ok = resolves(doi.rstrip("."))
        print(("OK  " if ok else "FAIL"), doi)
        if not ok:
            failures.append(doi)
        time.sleep(0.1)
    print(f"{len(dois) - len(failures)} of {len(dois)} DOIs resolved")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
