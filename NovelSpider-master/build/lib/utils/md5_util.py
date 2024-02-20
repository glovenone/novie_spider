import hashlib


def md5_util(content):
    text = content.encode("utf-8")
    m = hashlib.md5()
    m.update(text)
    return m.hexdigest()
