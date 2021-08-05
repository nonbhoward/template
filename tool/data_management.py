from common.paths import path
from json import dumps
from json import loads
from pathlib import Path
import logging
import os
import time
log = logging.getLogger(__name__)


class CacheAge:
    def __init__(self):
        self.MINUTE = 60
        self.HOUR = self.MINUTE * 60
        self.DAY = self.HOUR * 24
        self.WEEK = self.DAY * 7
        self.MONTH = self.DAY * 30
        self.YEAR = self.DAY * 365


class CacheType:
    def __init__(self):
        self.JSON = 'json'
        self.RAW = 'raw'
        self.OPTIONS = [self.JSON,
                        self.RAW]
        self.DEFAULT = self.JSON


class DefaultValue:
    def __init__(self):
        self.AGE_CACHE_STALE = AGE.HOUR
        self.FILEPATH = path.children['project']['data']


AGE = CacheAge()
CACHE_TYPE = CacheType()
DEFAULT = DefaultValue()


class CacheDataHandler:
    def __init__(self, cache_configuration, cache_filepath, cache_type=CACHE_TYPE.JSON):
        self._configuration = cache_configuration
        self._data = dict()
        self._filepath = cache_filepath \
            if isinstance(cache_filepath, Path) \
            else DEFAULT.FILEPATH
        self._readable = False
        if not self.configuration.get('seconds until stale', None):
            self._seconds_until_stale = DEFAULT.AGE_CACHE_STALE
        self._type = cache_type
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as cache:
                cache_raw = cache.read()
                cache_data = loads(cache_raw) \
                    if self.type is CACHE_TYPE.JSON \
                    else cache_raw
                data_unserialized = cache_data if cache_data else None
                self._data = data_unserialized
                self.readable = True if self.data else False
        log.info(f'{self.__class__.__name__} initialized with path {self.filepath}')

    def erase(self):
        os.remove(self.filepath)
        self._data = dict()
        self._readable = False

    def read(self):
        cache_file = self.filepath
        if not self._readable:
            print(f'cache data is not readable at {cache_file}')
            return
        with open(cache_file, 'r') as cache_file_to_read:
            log.info(f'loading json from file {cache_file}')
            data_unserialized = cache_file_to_read.read()
        self._data = data_unserialized

    def write(self, serializable_data=''):
        serializable_data = serializable_data if serializable_data else self.data
        data_to_write = dumps(serializable_data) \
            if self.type is CACHE_TYPE.JSON \
            else serializable_data
        write_location = self.filepath
        if os.path.exists(write_location):
            log.warning(f'overwriting file at {write_location}')
        with open(write_location, 'w') as file_to_write:
            log.info(f'writing to disk from {file_to_write}')
            file_to_write.write(data_to_write)
            self._data = loads(data_to_write) \
                if self.type is CACHE_TYPE.JSON \
                else data_to_write
            self._readable = True

    @property
    def age_seconds(self):
        creation_time_of_, exist = os.path.getmtime, os.path.exists
        time_create = creation_time_of_(self.filepath) if exist(self.filepath) else 0
        return time.time() - time_create

    @property
    def configuration(self):
        return self._configuration

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
        if not isinstance(value, int):
            log.warning(f'property must be set to type int, defaulting to {DEFAULT.AGE_CACHE_STALE} seconds')
            value = DEFAULT.AGE_CACHE_STALE
        self._seconds_until_stale = value

    @property
    def stale(self):
        return True if self.age_seconds > self.seconds_until_stale else False

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value not in CACHE_TYPE.OPTIONS:
            log.warning(f'bad value {value} for cache type, setting to default \n'
                        f'available types are : {CACHE_TYPE.OPTIONS}')
            value = CACHE_TYPE.DEFAULT
        self._type = value
