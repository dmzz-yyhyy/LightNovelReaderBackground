import json
import time
from threading import Thread

from utilities import is_time_over

from constant import MAX_CACHE


class Cache(Thread):
    def __init__(self):
        """
        :param func: 可调用的对象
        :param args: 可调用对象的参数
        """
        Thread.__init__(self)
        self.cache = {}
        self.last_update_time = time.time()
        self.last_key = ""

    def run(self):
        with open("cache.json", "r") as file:
            try:
                self.cache = json.loads(file.read())
            except:
                self.cache = {}
        while True:
            if is_time_over(self.last_update_time, 10):
                with open("cache.json", "r") as file:
                    try:
                        self.cache = json.loads(file.read())
                    except:
                        self.cache = {}
                if self.cache != {}:
                    for key in self.cache:
                        if is_time_over(self.cache[key][1], 240):
                            self.cache.pop(key)
                    with open("cache.json", "w") as file:
                        file.write(json.dumps(self.cache))
            time.sleep(60)


def save(uid, data):
    with open("cache.json", "r") as file:
        try:
            cache = json.loads(file.read())
        except:
            cache = {}
    with open("cache.json", "w+") as file:
        if len(cache) > MAX_CACHE:
            for key in cache:
                cache.pop(key)
                break
        cache[uid] = [data, time.time()]
        file.write(json.dumps(cache))


def get(uid):
    with open("cache.json", "r") as file:
        try:
            cache = json.loads(file.read())
        except:
            cache = {}
    if uid in cache:
        return cache.get(uid)[0]
    return None
