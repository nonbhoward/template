from constant.paths import path
from json import dumps
from json import loads
from pathlib import Path
import logging
import os
import time
log = logging.getLogger(__name__)


class CacheDataManager:
    def __init__(self, cache_filepath, json_cache=True):
        self._data = None
        self._filepath = cache_filepath if isinstance(cache_filepath, Path) else \
            Path(path.dirs['project']['data'], cache_filepath)
        self._is_json = True if json_cache else False
        self._readable = False
        self._seconds_until_stale = 600
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as cache:
                cache_raw = cache.read()
                cache_data = loads(cache_raw) if self.is_json else cache_raw
                data_unserialized = cache_data if cache_data else None
                self._data = data_unserialized
                self.readable = True if self.data else False
        log.info(f'{self.__class__.__name__} initialized with path {self.filepath}')

    def erase(self):
        os.remove(self.filepath)
        self._data = None
        self._readable = False

    def read(self):
        cache_file = self.filepath
        if not self._readable:
            print_and_log(f'cache data is not readable at {cache_file}', level=logging.WARNING)
            return None
        with open(cache_file, 'r') as cache_file_to_read:
            log.info(f'loading json from file {cache_file}')
            data_unserialized = cache_file_to_read.read()
        self._data = data_unserialized

    def write(self, serializable_data=''):
        serializable_data = serializable_data if serializable_data else self.data
        data_to_write = dumps(serializable_data) if self.is_json else serializable_data
        write_location = self.filepath
        if os.path.exists(write_location):
            log.warning(f'overwriting file at {write_location}')
        with open(write_location, 'w') as file_to_write:
            log.info(f'writing to disk from {file_to_write}')
            file_to_write.write(data_to_write)
            self._data = loads(data_to_write) if self.is_json else data_to_write
            self._readable = True

    @property
    def age_seconds(self):
        creation, exist = os.path.getmtime, os.path.exists
        time_create = creation(self.filepath) if exist(self.filepath) else 0
        time_now = time.time()
        return time_now - time_create

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self.write(serializable_data=value)

    @property
    def filepath(self):
        return self._filepath

    @property
    def is_json(self):
        return self._is_json

    @property
    def readable(self):
        return self._readable

    @readable.setter
    def readable(self, value):
        log.warning(f'do not assign a value to {self.__class__.__name__}.readable manually')
        self._readable = value if isinstance(value, bool) else False

    @property
    def seconds_until_stale(self):
        return self._seconds_until_stale

    @seconds_until_stale.setter
    def seconds_until_stale(self, value):
        default_value = 600
        value_is_int = True if isinstance(value, int) else False
        if not value_is_int:
            log.warning(f'property must be set to type int, defaulting to {default_value} minutes')
        self._seconds_until_stale = value if value_is_int else default_value

    @property
    def stale(self):
        return True if self.age_seconds > self.seconds_until_stale else False


def print_and_log(message, level=logging.INFO):
    print(f'{logging.getLevelName(level)} {message}')
    log.log(level=level, msg=message)
