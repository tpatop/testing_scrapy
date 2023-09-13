import hashlib


def hash_text(text) -> str:
    if text is not None:
        f = hashlib.sha224()
        f.update(text.encode())
        return f.hexdigest()
