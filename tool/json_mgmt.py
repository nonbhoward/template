from constant.names import fn_json
from constant.paths import path
from json import dumps
from json import loads
from pathlib import Path
import logging
import os
import time
log = logging.getLogger(__name__)


class JsonManager:
    def __init__(self, data='', filepath=''):
        """
        :param data: path or data
        :param filepath: optional filepath, use to manage multiple cache in parallel
        """
        jsm = self.__class__.__name__
        # init
        if not os.path.exists(filepath):
            print(f'{filepath} does not exist')
            with open(filepath, 'w') as ftw:
                ftw.write(dumps(''))
        self.cache = filepath
        # startup
        self.data = data if data else None
        try:
            self.data = self.read(data) if is_path_(data) else self.read()
        except Exception as exc:
            for xarg in exc.args:
                log.error(f'{xarg}')
            print(f'error instantiating {jsm}')
        log.info(f'{jsm} initialized with path {self.cache}')

    def clear_cache(self):
        os.remove(self.cache)
        self._data = ''

    def read(self, file='') -> dict:
        file = self.cache if not file else file
        if not os.path.exists(file):
            log.warning(f'required path does not exist at {file}')
            return {}
        with open(file, 'r') as jf:
            log.info(f'loading json from file {file}')
            contents = loads(jf.read())
        return contents

    def write(self, data=''):
        data = data if data else self._data
        file_to_write = self.cache
        if os.path.exists(file_to_write):
            log.warning(f'overwriting file at {file_to_write}')
        with open(file_to_write, 'w') as ftw:
            log.info(f'writing to disk from {ftw}')
            ftw.write(dumps(data))

    @property
    def cache(self):
        return self._path_to_data

    @cache.setter
    def cache(self, value):
        self._path_to_data = value

    @property
    def cache_age_hours(self):
        time_create = os.path.getmttime(self.cache) if os.path.exists(self.cache) else 0
        time_now = time.time()
        cache_age = time_now - time_create
        return cache_age / 3600

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        # FIXME can cause excessive writes, re-work (resolved)
        if value is not None:
            # self.write(value)
            pass
        self._data = value


def is_dict_(item) -> bool:
    return True if isinstance(item, dict) else False


def is_path_(item) -> bool:
    return True if isinstance(item, Path) else False
