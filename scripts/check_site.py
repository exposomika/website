"""Dependency-free smoke check for the rendered static site and deployment assets."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

root = Path(__file__).resolve().parents[1] / "docs"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.references = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.references.append(attrs[key])
        if tag == "img":
            self.images.append(attrs)


page = SiteParser()
page.feed((root / "index.html").read_text())
assert len(page.ids) == len(set(page.ids)), "Duplicate HTML IDs"
for ref in page.references:
    url = urlsplit(ref)
    if url.scheme or url.netloc:
        continue
    if url.path:
        assert (root / unquote(url.path).lstrip("/")).is_file(), f"Missing file: {ref}"
    if url.fragment and not url.path:
        assert unquote(url.fragment) in page.ids, f"Missing anchor: {ref}"
for img in page.images:
    assert "alt" in img, f"Image missing alternative text: {img}"
for ref in re.findall(r"url\(['\"]?([^)'\"]+)", (root / "styles.css").read_text()):
    if not urlsplit(ref).scheme:
        assert (root / ref).is_file(), f"Missing CSS asset: {ref}"
assert (root / "CNAME").read_text().strip() == "exposomika.io"
assert (root / ".nojekyll").is_file(), "Missing .nojekyll"
assert "mailto:hello@exposomika.io" in page.references
print(f"Passed: {len(page.references)} references, {len(page.images)} images, anchors, CSS assets, contact and domain.")
