"""
535. Encode and Decode TinyURLs
"""
import string

class Codec:
    """
    Codec that encodes long URLs to short ones and decodes short URLs back.
    Uses an incremental integer id and base62 encoding for stable, collision-free keys.
    """

    ALPHABET = string.ascii_letters + string.digits  # 26+26+10 = 62 chars
    BASE = len(ALPHABET)
    PREFIX = "http://tinyurl.com/"

    def __init__(self):
        self.id_to_long = {}
        self.long_to_id = {}
        self.counter = 1  # start from 1 to avoid empty key

    def _encode_id(self, n: int) -> str:
        # convert integer to base62 string
        if n == 0:
            return self.ALPHABET[0]
        chars = []
        while n > 0:
            n, rem = divmod(n, self.BASE)
            chars.append(self.ALPHABET[rem])
        return ''.join(reversed(chars))

    def encode(self, longUrl: str) -> str:
        # if already encoded, return existing short
        if longUrl in self.long_to_id:
            key = self._encode_id(self.long_to_id[longUrl])
            return self.PREFIX + key

        # assign new id
        uid = self.counter
        self.counter += 1

        self.long_to_id[longUrl] = uid
        self.id_to_long[uid] = longUrl

        key = self._encode_id(uid)
        return self.PREFIX + key

    def decode(self, shortUrl: str) -> str:
        # extract key after prefix
        if not shortUrl.startswith(self.PREFIX):
            return ""  # or raise ValueError("invalid short url")
        key = shortUrl[len(self.PREFIX):]

        # decode base62 key back to integer id
        uid = 0
        for ch in key:
            uid = uid * self.BASE + self.ALPHABET.index(ch)

        return self.id_to_long.get(uid, "")
