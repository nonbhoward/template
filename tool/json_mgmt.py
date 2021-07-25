from constant.paths import path
from json import dumps
from json import loads
from pathlib import Path
import logging
import os
import time
log = logging.getLogger(__name__)


class JsonDataManager:
    def __init__(self, cache_filepath):
        """
        a class handling common json file interactions
        :param cache_filepath: the address of the cache file on disk"""
        # init
        project_data_path = path.dirs['project']['data']
        self._filepath = cache_filepath \
            if isinstance(cache_filepath, Path) else Path(project_data_path, cache_filepath)
        self._data = None
        self._cache_able_to_be_read = False
        self._refresh_age_threshold = 600
        # check if cache is readable
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as cache:
                cache_contents = cache.read()
                data_unserialized = cache_contents if cache_contents else None
                self.data = data_unserialized
                self.readable = True if self.data else False
        log.info(f'{self.__class__.__name__} initialized with path {self.filepath}')

    def erase(self):
        """
        delete cache file from system, set class cache data to None
        :return: None
        """
        os.remove(self.filepath)
        self.data = None
        self.readable = False

    def read(self):
        """
        conditions for reading json cache data
        1. cache data not readable, log warning, return None
        2. cache data readable, return ??
        :return: None
        """
        cache_file = self.filepath
        if not self.readable:
            print_and_log(f'cache data is not readable at {cache_file}', level=logging.WARNING)
            return None
        with open(cache_file, 'r') as json_file:
            log.info(f'loading json from file {cache_file}')
            data_unserialized = loads(json_file.read())
        self.data = data_unserialized

    def write(self, serializable_data):
        """
        :param serializable_data: serializable data to dump to json and write to disk
        :return: None
        """
        data_serialized = dumps(serializable_data)
        cache_file = self.filepath
        if os.path.exists(cache_file):
            log.warning(f'overwriting file at {cache_file}')
        with open(cache_file, 'w') as json_file:
            log.info(f'writing to disk from {json_file}')
            json_file.write(data_serialized)
            self.data = data_serialized
            self.readable = True

    @property
    def age(self):
        time_create = os.path.getmtime(self.filepath) \
            if os.path.exists(self.filepath) else 0
        time_now = time.time()
        return time_now - time_create

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def filepath(self):
        return self._filepath

    @property
    def readable(self):
        return self._cache_able_to_be_read

    @readable.setter
    def readable(self, value):
        default_value = False
        value_is_boolean = True if isinstance(value, bool) else False
        if not value_is_boolean:
            log.warning(f'property must be set to type boolean, defaulting to {default_value}')
        self._cache_able_to_be_read = value if value_is_boolean else default_value

    @property
    def refresh_age_threshold(self):
        return self._refresh_age_threshold

    @refresh_age_threshold.setter
    def refresh_age_threshold(self, value):
        default_value = 600  # seconds
        value_is_int = True if isinstance(value, int) else False
        if not value_is_int:
            log.warning(f'property must be set to type int, defaulting to {default_value} minutes')
        self._refresh_age_threshold = value if value_is_int else default_value

    @property
    def stale(self):
        return True if self.age > self.refresh_age_threshold else False


def print_and_log(message, level=logging.INFO):
    print(f'{logging.getLevelName(level)} {message}')
    log.log(level=level, msg=message)
