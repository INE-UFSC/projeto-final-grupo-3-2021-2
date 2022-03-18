from abc import ABC
import json


class DAO(ABC):
    def __init__(self, datasource='') -> None:
        self.__datasource = datasource
        self.__objectCache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        with open(self.__datasource, 'w') as f:
            json.dump(self.__objectCache, f)

    def __load(self):
        with open(self.__datasource, 'r') as f:
            self.__objectCache = json.load(f)

    def add(self, key, obj):
        self.__objectCache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__objectCache[key]
        except KeyError:
            return None

    def remove(self, key):
        try:
            self.__objectCache.pop(key)
            self.__dump()
        except KeyError:
            return None

    def get_all(self):
        return self.__objectCache
