import json
import os
from . import JsonCore as jCore
import hashlib


def get_cache(uid):
    try:
        return jCore.read_json("cache/cache.json")[uid]
    except FileNotFoundError:
        os.makedirs(os.path.dirname("cache/cache.json"), exist_ok=True)
        jCore.write_to_json("cache/cache.json", {})
        return None
    except KeyError:
        return None


def set_cache(uid, output):
    data = jCore.read_json("cache/cache.json")
    data[uid] = output
    jCore.write_to_json("cache/cache.json", data)


def cache(func_to_cache):
    def wrapper(*args):
        uid = hashlib.sha256(("".join(str(i) for i in args)).encode()).hexdigest()
        output = get_cache(uid)
        if not output:
            output = func_to_cache(*args)
            set_cache(uid, output)
        return output
    return wrapper
