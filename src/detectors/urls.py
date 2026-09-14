import re
from urllib.parse import urlparse


url_pattern = re.compile(r"https?://[^\s<>()]+|www\.[^\s<>()]+", re.IGNORECASE)
shortener_domains = {"bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "ow.ly"}
known_brands = {"paypal", "microsoft", "apple", "amazon", "netflix", "instagram"}


def detect_suspicious_urls(message):
    matches = []
    for raw_url in url_pattern.findall(message):
        url = raw_url.rstrip(".,!?;:")
        parsed = urlparse(url if "://" in url else f"http://{url}")
        hostname = (parsed.hostname or "").lower()
        reason = None

        if not hostname:
            continue
        if hostname.startswith("xn--") or ".xn--" in hostname:
            reason = f"punycode domain ({hostname})"
        elif re.fullmatch(r"\d+(?:\.\d+){3}", hostname):
            reason = f"IP-address URL ({hostname})"
        elif hostname in shortener_domains:
            reason = f"shortened URL ({hostname})"
        else:
            labels = set(hostname.replace("-", ".").split("."))
            for brand in known_brands:
                if any(label.startswith(brand) and label != brand for label in labels):
                    reason = f"lookalike brand domain ({hostname})"
                    break

        if reason:
            matches.append(reason)
    return matches